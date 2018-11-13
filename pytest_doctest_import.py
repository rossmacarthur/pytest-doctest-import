import pytest


__version__ = '0.1.0'


def pad(l, until=0, fillvalue=None):
    """
    Pad a list.
    """
    for _ in range(until - len(l)):
        l.insert(0, fillvalue)

    return l


def rpad(l, until=0, fillvalue=None):
    """
    Right pad a list.
    """
    for _ in range(until - len(l)):
        l.append(fillvalue)

    return l


def split_exact(s, sep=None, split=0, fillvalue=None):
    """
    Split a string an exact amount of times.
    """
    return rpad(s.split(sep, split), split + 1, fillvalue=fillvalue)


def rsplit_exact(s, sep=None, split=0, fillvalue=None):
    """
    Split a string an exact amount of times.

    Splits are done starting at the end of the string and working to the front.
    """
    return pad(s.rsplit(sep, split), split + 1, fillvalue=fillvalue)


def import_option(name, namespace, from_operator='<', as_operator='@'):
    """
    Try import the given module.

    The name of the module must following the following custom syntax:

    The syntax is
      - `<` is used for `from ... import ...` imports.
      - `@` is used for importing something with a different name like when
        using the `as` operator.

    For example
      - To `import package` use `package`.
      - To `import package.module` use `package.module`.
      - To `import package as mypackage` use `package@mypackage`.
      - To `from package import *` use `*<package`.
      - To `from package import module` use `module<package`.
      - To `from package import module as mymodule` use `module@mymodule<package`.
      - To `from package import a as x, b as y` use `a@x,b@y<package`.

    .. doctest::

        >>> ns = {}
        >>> import_option('pytest@mypytest', namespace=ns)
        >>> assert 'mypytest' in ns
        >>> assert isinstance(ns['mypytest'], ModuleType)

    Args:
        name (str): the import name following the custom syntax.
        namespace (dict): the namespace to add the imports to.
        from_operator (str): the operator to use for the "from" syntax.
        as_operator (str): the operator to use for the "as" syntax.
    """
    as_name = None
    fromlist = None

    extracts, name = rsplit_exact(name, from_operator, 1, '')
    extracts = [split_exact(f, as_operator, 1) for f in extracts.split(',') if f]
    fromlist = [f[0] for f in extracts] or None
    name, as_name = split_exact(name, as_operator, 1)

    module = __import__(name, globals=namespace, fromlist=fromlist, level=0)

    if fromlist:
        if '*' in fromlist:
            if hasattr(module, '__all__'):
                all_names = zip(module.__all__, module.__all__)
            else:
                all_names = ((name, name) for name in dir(module) if not name.startswith('_'))
        else:
            all_names = extracts

        namespace.update({as_name or name: getattr(module, name) for name, as_name in all_names})
    else:
        namespace[as_name or name.split('.')[0]] = module


@pytest.fixture(autouse=True)
def doctest_import(request, doctest_namespace):
    """
    Import the specified modules.

    This fixture imports each name given and adds it to the doctest namespace.

    The syntax is
      - `<` is used for `from ... import ...` imports.
      - `@` is used for importing something with a different name like when
        using the `as` operator.

    Examples:

        --doctest-modules --doctest-import "package"
        --doctest-modules --doctest-import "package@mypackage"
        --doctest-modules --doctest-import "package.module"
        --doctest-modules --doctest-import "*<package"
        --doctest-modules --doctest-import "module<package"
        --doctest-modules --doctest-import "module@mymodule<mypackage"
    """
    for name in request.config.getoption('--doctest-import'):
        import_option(name, namespace=doctest_namespace)


def pytest_addoption(parser):
    """
    Add the `--doctest-import` option.
    """
    parser.addoption(
        '--doctest-import',
        nargs='+',
        default=[],
        help='A list of names to import.'
    )
