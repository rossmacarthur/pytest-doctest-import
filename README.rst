pytest-doctest-import
=====================

A simple pytest plugin to import names and add them to the doctest namespace.

Installing
----------

Install this package with

::

    pip install pytest-doctest-import


Usage
-----

Simply pass the import names to ``--doctest-import`` when instantiating `pytest`.

To get the equivalent of ``import package.module`` use

::

    pytest --doctest-modules --doctest-import "package.module"


To get the equivalent of ``from package import *`` use

::

    pytest --doctest-modules --doctest-import "*<package"


To get the equivalent of ``from package import module as mymodule`` use

::

    pytest --doctest-modules --doctest-import "module@mymodule<package"


License
-------

This project is licensed under the MIT License.
