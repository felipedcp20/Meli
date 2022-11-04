import pymysql
from fastapi import HTTPException



def connection_db (host,user,passwd):
    """function to create coneccion with db Mysql"""

    try:
        connection = pymysql.connect(
            host=host,
            user=user,
            passwd=passwd,
        )


        return (True,connection)


    except pymysql.err.OperationalError as e:
        return HTTPException(status_code=404, detail=f"{e}")
