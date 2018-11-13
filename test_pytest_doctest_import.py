import six
import sys

# This is a hack so pytest-cov works correctly.
del sys.modules['pytest_doctest_import']  # noqa: E402

from pytest_doctest_import import pad, rpad, split_exact, rsplit_exact, import_option


def test_pad():
    case = [1, 2, 3]
    result = pad(case, until=5, fillvalue=0)
    assert result is case
    assert result == [0, 0, 1, 2, 3]


def test_rpad():
    case = [1, 2, 3]
    result = rpad(case, until=5, fillvalue=0)
    assert result is case
    assert result == [1, 2, 3, 0, 0]


def test_split_exact():
    assert split_exact('a', ',', 1, fillvalue='') == ['a', '']
    assert split_exact('a,a', ',', 1, fillvalue='') == ['a', 'a']
    assert split_exact('a,a', ',', 2, fillvalue='') == ['a', 'a', '']
    assert split_exact('a,a', ',', 3, fillvalue='') == ['a', 'a', '', '']


def test_rsplit_exact():
    assert rsplit_exact('a', ',', 1, fillvalue='') == ['', 'a']
    assert rsplit_exact('a,a', ',', 1, fillvalue='') == ['a', 'a']
    assert rsplit_exact('a,a', ',', 2, fillvalue='') == ['', 'a', 'a']
    assert rsplit_exact('a,a', ',', 3, fillvalue='') == ['', '', 'a', 'a']


def test_import_option():
    ns = {}

    import_option('six', ns)
    assert ns['six'] == six

    import_option('six@seven', ns)
    assert ns['seven'] == six

    import_option('with_metaclass<six', ns)
    assert ns['with_metaclass'] == six.with_metaclass

    import_option('with_metaclass@derp<six', ns)
    assert ns['derp'] == six.with_metaclass

    import_option('*<six', ns)
    assert len(ns) > 30
