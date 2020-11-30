import io
import os
import re
from setuptools import setup


def read(*path):
    """
    Cross-platform Python 2/3 file reading.
    """
    filename = os.path.join(os.path.dirname(__file__), *path)
    return io.open(filename, encoding='utf8').read()


def find_version():
    """
    Regex search __init__.py so that we do not have to import.
    """
    text = read('pytest_doctest_import.py')
    match = re.search(r'^__version__ = [\'"]([^\'"]*)[\'"]', text, re.M)

    if match:
        return match.group(1)

    raise RuntimeError('Unable to find version string.')


version = find_version()

url = 'https://github.com/rossmacarthur/pytest-doctest-import'

long_description = read('README.rst')

install_requirements = [
    'pytest>=3.6.0'
]

lint_requirements = [
    'flake8<3.8.0',
    'flake8-quotes',
    'pep8-naming'
]

test_requirements = [
    'pytest-cov',
    'six'
]

setup(
    name='pytest-doctest-import',
    py_modules=['pytest_doctest_import'],
    version=version,
    install_requires=install_requirements,
    extras_require={
        'linting': lint_requirements,
        'testing': test_requirements
    },
    python_requires='>=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*',
    entry_points={
        'pytest11': [
            'doctest-import = pytest_doctest_import',
        ],
    },

    author='Ross MacArthur',
    author_email='macarthur.ross@gmail.com',
    maintainer='Ross MacArthur',
    maintainer_email='macarthur.ross@gmail.com',
    description='A simple pytest plugin to import names and add them to the doctest namespace.',
    long_description=long_description,
    license='MIT',
    url=url,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Framework :: Pytest',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Testing',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Operating System :: OS Independent',
        'License :: OSI Approved :: MIT License',
    ]
)
