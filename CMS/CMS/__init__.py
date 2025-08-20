# Optional: allow PyMySQL as a drop-in replacement for mysqlclient
try:
    import MySQLdb  # type: ignore
except Exception:
    try:
        import pymysql  # type: ignore
        pymysql.install_as_MySQLdb()
    except Exception:
        # If neither package is available, Django will raise a clear error when connecting
        pass
