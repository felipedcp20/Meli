import pymysql
from fastapi import HTTPException


def connection_dbMysql(host, user, passwd):
    """function to create coneccion with db Mysql"""

    try:
        connection = pymysql.connect(
            host=host,
            user=user,
            passwd=passwd,
        )
        cursor = connection.cursor()
        return cursor

    except pymysql.err.OperationalError as e:
        raise HTTPException(status_code=404, detail=f"{e}") from e
