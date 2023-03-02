from sqlalchemy.dialects.postgresql.asyncpg import PGDialect_asyncpg

from sqlalchemy_postgresql_relaxed.base import PGDialect_relaxed


class PGDialect_asyncpg_relaxed(PGDialect_relaxed, PGDialect_asyncpg):
    """
    Don't strictly expect JSON and JSONB codecs.

    asyncpg.exceptions._base.InterfaceError: cannot use custom codec on non-scalar type pg_catalog.json
    """

    driver = "asyncpg_relaxed"
    supports_statement_cache = True

    async def setup_asyncpg_json_codec(self, conn):
        pass

    async def setup_asyncpg_jsonb_codec(self, conn):
        pass


dialect = PGDialect_asyncpg_relaxed
