.. image:: https://github.com/daq-tools/sqlalchemy-postgresql-relaxed/workflows/Tests/badge.svg
    :target: https://github.com/daq-tools/sqlalchemy-postgresql-relaxed/actions?workflow=Tests

.. image:: https://codecov.io/gh/daq-tools/sqlalchemy-postgresql-relaxed/branch/main/graph/badge.svg
    :target: https://codecov.io/gh/daq-tools/sqlalchemy-postgresql-relaxed
    :alt: Test suite code coverage

.. image:: https://pepy.tech/badge/sqlalchemy-postgresql-relaxed/month
    :target: https://pepy.tech/project/sqlalchemy-postgresql-relaxed

.. image:: https://img.shields.io/pypi/v/sqlalchemy-postgresql-relaxed.svg
    :target: https://pypi.org/project/sqlalchemy-postgresql-relaxed/

.. image:: https://img.shields.io/pypi/status/sqlalchemy-postgresql-relaxed.svg
    :target: https://pypi.org/project/sqlalchemy-postgresql-relaxed/

.. image:: https://img.shields.io/pypi/pyversions/sqlalchemy-postgresql-relaxed.svg
    :target: https://pypi.org/project/sqlalchemy-postgresql-relaxed/

.. image:: https://img.shields.io/pypi/l/sqlalchemy-postgresql-relaxed.svg
    :target: https://github.com/daq-tools/sqlalchemy-postgresql-relaxed/blob/main/LICENSE

|

##########################################
Relaxed PostgreSQL dialects for SQLAlchemy
##########################################


*****
About
*****

The vanilla dialects for connecting to PostgreSQL with SQLAlchemy will employ
a few behaviors that strictly expect a PostgreSQL server on the other end.
However, some operations may croak on databases which only offer
wire-compatibility with PostgreSQL.

The dialects provided by ``sqlalchemy-postgresql-relaxed`` are building upon
the vanilla SQLAlchemy dialects, but will disable a few PostgreSQL specifics.

- ``postgresql+psycopg``: Accept non-conforming server version responses.
- ``postgresql+psycopg``: Don't issue ``SHOW STANDARD_CONFORMING_STRINGS`` inquiry.
- ``postgresql+asyncpg``: Don't strictly expect JSON and JSONB codecs.


*****
Usage
*****

The corresponding dialect identifiers are:

- ``postgresql+psycopg_relaxed``
- ``postgresql+asyncpg_relaxed``

They can be used within SQLAlchemy database URL identifiers as usual.

.. code-block:: python

    # psycopg synchronous
    create_engine(
        url="postgresql+psycopg_relaxed://crate@localhost/acme",
        isolation_level="AUTOCOMMIT",
        use_native_hstore=False)

    # psycopg asynchronous
    create_async_engine(
        url="postgresql+psycopg_relaxed://crate@localhost/acme",
        isolation_level="AUTOCOMMIT",
        use_native_hstore=False)

    # asyncpg
    create_async_engine(
        url="postgresql+asyncpg_relaxed://crate@localhost/acme",
        isolation_level="AUTOCOMMIT")


*****
Setup
*****
::

    pip install --upgrade sqlalchemy-postgresql-relaxed

To install the latest development version from the repository, invoke::

    pip install --upgrade git+https://github.com/daq-tools/sqlalchemy-postgresql-relaxed


*******************
Project information
*******************

Contributions
=============

Every kind of contribution, feedback, or patch, is much welcome. `Create an
issue`_ or submit a patch if you think we should include a new feature, or to
report or fix a bug.

Development
===========

In order to setup a development environment on your workstation, please head over
to the `development sandbox`_ documentation. When you see the software tests succeed,
you should be ready to start hacking.

Resources
=========

- `Source code repository <https://github.com/daq-tools/sqlalchemy-postgresql-relaxed>`_
- `Documentation <https://github.com/daq-tools/sqlalchemy-postgresql-relaxed/blob/main/README.rst>`_
- `Python Package Index (PyPI) <https://pypi.org/project/sqlalchemy-postgresql-relaxed/>`_

License and warranty
====================

The project is licensed under the terms of the MIT license, see `LICENSE`_.


.. _Create an issue: https://github.com/daq-tools/sqlalchemy-postgresql-relaxed/issues/new
.. _development sandbox: https://github.com/daq-tools/sqlalchemy-postgresql-relaxed/blob/main/DEVELOP.rst
.. _LICENSE: https://github.com/daq-tools/sqlalchemy-postgresql-relaxed/blob/main/LICENSE
