from sqlalchemy.dialects.postgresql.psycopg import PGDialect_psycopg, PGDialectAsync_psycopg

from sqlalchemy_postgresql_relaxed.base import PGDialect_relaxed


class PGDialect_psycopg_relaxed(PGDialect_relaxed, PGDialect_psycopg):
    driver = "psycopg_relaxed"

    @classmethod
    def get_async_dialect_cls(cls, url):
        return PGDialectAsync_psycopg_relaxed


class PGDialectAsync_psycopg_relaxed(PGDialect_psycopg_relaxed, PGDialectAsync_psycopg):
    is_async = True
    supports_statement_cache = True
    driver = "psycopg_async_relaxed"


dialect = PGDialect_psycopg_relaxed
dialect_async = PGDialectAsync_psycopg_relaxed
