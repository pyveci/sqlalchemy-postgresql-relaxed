import sys

import pandas as pd
import pytest
import sqlalchemy as sa
from pandas._testing import assert_frame_equal
from sqlalchemy.ext.asyncio import create_async_engine

REFERENCE_FRAME = pd.DataFrame.from_records([{"mountain": "Mont Blanc", "height": 4808}])
SQL_SELECT_STATEMENT = "SELECT mountain, height FROM sys.summits ORDER BY height DESC LIMIT 1;"


if sys.version_info < (3, 8):
    pytest.skip("Does not work on Python 3.7", allow_module_level=True)


def test_crate_read_sql(cratedb_http_host, cratedb_http_port):
    engine = sa.create_engine(
        url=f"crate://{cratedb_http_host}:{cratedb_http_port}",
        echo=True,
    )
    conn = engine.connect()
    df = pd.read_sql(sql=sa.text(SQL_SELECT_STATEMENT), con=conn)
    assert_frame_equal(df, REFERENCE_FRAME)


def test_psycopg_read_sql(cratedb_psql_host, cratedb_psql_port):
    engine = sa.create_engine(
        url=f"postgresql+psycopg_relaxed://crate@{cratedb_psql_host}:{cratedb_psql_port}",
        isolation_level="AUTOCOMMIT",
        use_native_hstore=False,
        echo=True,
    )
    conn = engine.connect()
    df = pd.read_sql(sql=sa.text(SQL_SELECT_STATEMENT), con=conn)
    assert_frame_equal(df, REFERENCE_FRAME)


@pytest.mark.asyncio
async def test_psycopg_async_read_sql(cratedb_psql_host, cratedb_psql_port):
    engine = create_async_engine(
        url=f"postgresql+psycopg_relaxed://crate@{cratedb_psql_host}:{cratedb_psql_port}",
        isolation_level="AUTOCOMMIT",
        use_native_hstore=False,
        echo=True,
    )

    async with engine.begin() as conn:
        df = await conn.run_sync(read_sql_sync, sa.text(SQL_SELECT_STATEMENT))
        assert_frame_equal(df, REFERENCE_FRAME)


@pytest.mark.asyncio
async def test_asyncpg_read_sql(cratedb_psql_host, cratedb_psql_port):
    engine = create_async_engine(
        url=f"postgresql+asyncpg_relaxed://crate@{cratedb_psql_host}:{cratedb_psql_port}",
        isolation_level="AUTOCOMMIT",
        echo=True,
    )

    async with engine.begin() as conn:
        df = await conn.run_sync(read_sql_sync, sa.text(SQL_SELECT_STATEMENT))
        assert_frame_equal(df, REFERENCE_FRAME)


def read_sql_sync(conn, stmt):
    """
    Making pd.read_sql connection the first argument to make it compatible
    with conn.run_sync(), see https://stackoverflow.com/a/70861276.
    """
    return pd.read_sql(stmt, conn)
