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


def querymysql(query, cursor):
    """_summary_

    Args:
        query (str): "Query for Sql"
        cursor (objct cursor): cursor with conection sql

    Returns:
        str: result to consult query
    """
    cursor.execute(query)
    result_fetch = cursor.fetchall()
    result = []
    for element in result_fetch:
        result.append(element[0])

    return result


def clasificationdb(listofdatabases, cursor):
    """generate clasificatioDb"""

    response = []

    for database in listofdatabases:
        cursor.execute(f"USE {database}")
        tables = querymysql("show tables", cursor)

        for table in tables:
            columns = querymysql(f"show columns from {table}", cursor)
            tables_column = (database, table, columns)
            response.append(tables_column)

    return response
