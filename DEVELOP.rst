.. highlight: console

#######################
Development information
#######################


************
Introduction
************

The test suite demonstrates the use of the "relaxed" variants of SQLAlchemy's
builtin PostgreSQL support by connecting to databases which are protocol
compatible with PostgreSQL.


*****
Setup
*****

Currently, `CrateDB`_ is used. The easiest way to provide an instance to the
test suite, is::

    docker run --rm -it --publish=4200:4200 --publish=5432:5432 crate/crate:nightly

For installing the package inside a development sandbox (virtualenv), run::

    git clone https://github.com/pyveci/sqlalchemy-postgresql-relaxed
    cd sqlalchemy-postgresql-relaxed
    python3 -m venv .venv
    source .venv/bin/activate
    pip install --editable=.[develop,test]


*****
Check
*****

To run all validation steps (linter, software tests), invoke::

    poe check


*******
Release
*******

In order to prepare for building and publishing release packages, run::

    pip install --editable=.[release]

Then, it is mostly as easy as::

    poe release


.. _CrateDB: https://github.com/crate/crate
