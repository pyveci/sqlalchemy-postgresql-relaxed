import pytest
import sqlalchemy as sa
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine


def test_psycopg_sync():
    engine = sa.create_engine(
        url="postgresql+psycopg_relaxed://crate@localhost/acme",
        isolation_level="AUTOCOMMIT",
        use_native_hstore=False,
        echo=True,
    )
    with engine.connect() as con:
        result = con.exec_driver_sql("SELECT 'Kill all humans.';")
        assert result.scalar_one() == "Kill all humans."
    con.close()


@pytest.mark.asyncio
async def test_psycopg_async():
    engine = create_async_engine(
        url="postgresql+psycopg_relaxed://crate@localhost/acme",
        isolation_level="AUTOCOMMIT",
        use_native_hstore=False,
        echo=True,
    )
    async_session = async_sessionmaker(engine)
    session: AsyncSession
    async with async_session() as session:
        result = await session.execute(sa.text("SELECT 'Kill all humans.';"))
        assert result.scalar_one() == "Kill all humans."
    await session.close()
    await engine.dispose()


@pytest.mark.asyncio
async def test_asyncpg():
    engine = create_async_engine(
        url="postgresql+asyncpg_relaxed://crate@localhost/acme",
        isolation_level="AUTOCOMMIT",
        echo=True,
    )
    async_session = async_sessionmaker(engine)
    session: AsyncSession
    async with async_session() as session:
        result = await session.execute(sa.text("SELECT 'Kill all humans.';"))
        assert result.scalar_one() == "Kill all humans."
    await session.close()
    await engine.dispose()
