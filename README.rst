pytest-doctest-import
=====================

.. image:: https://img.shields.io/pypi/v/pytest-doctest-import.svg?style=flat-square&colorB=4c1
    :target: https://pypi.org/project/pytest-doctest-import/
    :alt: PyPI Version

.. image:: https://img.shields.io/travis/rossmacarthur/pytest-doctest-import/master.svg?style=flat-square
    :target: https://travis-ci.org/rossmacarthur/pytest-doctest-import
    :alt: Build Status

.. image:: https://img.shields.io/codecov/c/github/rossmacarthur/pytest-doctest-import.svg?style=flat-square
    :target: https://codecov.io/gh/rossmacarthur/pytest-doctest-import
    :alt: Code Coverage

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
