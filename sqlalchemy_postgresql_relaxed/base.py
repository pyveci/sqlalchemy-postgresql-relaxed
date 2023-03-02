import re

from sqlalchemy.dialects.postgresql.base import PGDialect
from sqlalchemy.engine.default import DefaultDialect


class PGDialect_relaxed(PGDialect):
    def _get_server_version_info(self, connection):
        """
        Accept non-conforming server version responses by adjusting signature matching pattern.

        AssertionError: Could not determine version from string
        'CrateDB 5.2.2 (built a33862e/2023-02-09T10:26:09Z, Linux 5.10.124-linuxkit amd64, OpenJDK 64-Bit Server VM 19.0.2+7)'
        """  # noqa: E501
        v = connection.exec_driver_sql("select pg_catalog.version()").scalar()
        m = re.match(
            r".*(?:PostgreSQL|EnterpriseDB|\w+?) " r"(\d+)\.?(\d+)?(?:\.(\d+))?(?:\.\d+)?(?:devel|beta)?",
            v,
        )
        if not m:
            raise AssertionError("Could not determine version from string '%s'" % v)
        return tuple([int(x) for x in m.group(1, 2, 3) if x is not None])

    def initialize(self, connection):
        """
        Don't issue `SHOW STANDARD_CONFORMING_STRINGS` inquiry.

        sqlalchemy.exc.InternalError: (psycopg.errors.InternalError_)
        Unknown session setting name 'standard_conforming_strings'.
        """
        DefaultDialect.initialize(self, connection)

        # https://www.postgresql.org/docs/9.3/static/release-9-2.html#AEN116689
        self.supports_smallserial = self.server_version_info >= (9, 2)

        # PATCH. Let's assume "on"?
        """
        std_string = connection.exec_driver_sql(
            "show standard_conforming_strings"
        ).scalar()
        """
        std_string = "on"

        self._backslash_escapes = std_string == "off"

        self._supports_drop_index_concurrently = self.server_version_info >= (
            9,
            2,
        )
        self.supports_identity_columns = self.server_version_info >= (10,)
