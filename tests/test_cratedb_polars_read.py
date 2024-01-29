import sys

import polars as pl
import pytest
import sqlalchemy as sa
from polars.testing import assert_frame_equal

REFERENCE_FRAME = pl.from_records([{"mountain": "Mont Blanc", "height": 4808}])
SQL_SELECT_STATEMENT = "SELECT mountain, height FROM sys.summits ORDER BY height DESC LIMIT 1;"


if sys.version_info < (3, 8):
    pytest.skip("Does not work on Python 3.7", allow_module_level=True)


def test_crate_read_sql(cratedb_http_host, cratedb_http_port):
    engine = sa.create_engine(
        url=f"crate://{cratedb_http_host}:{cratedb_http_port}",
        echo=True,
    )
    conn = engine.connect()
    df = pl.read_database(
        query=SQL_SELECT_STATEMENT,
        connection=conn,
        schema_overrides={"value": pl.Utf8},
    )
    assert_frame_equal(df, REFERENCE_FRAME)


def test_psycopg_read_sql(cratedb_psql_host, cratedb_psql_port):
    engine = sa.create_engine(
        url=f"postgresql+psycopg_relaxed://crate@{cratedb_psql_host}:{cratedb_psql_port}",
        isolation_level="AUTOCOMMIT",
        use_native_hstore=False,
        echo=True,
    )
    conn = engine.connect()
    df = pl.read_database(
        query=SQL_SELECT_STATEMENT,
        connection=conn,
        schema_overrides={"value": pl.Utf8},
    )
    assert_frame_equal(df, REFERENCE_FRAME)
