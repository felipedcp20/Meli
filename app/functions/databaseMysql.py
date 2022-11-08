import re
import pymysql

from fastapi import HTTPException


keywords = [
    ("credit", "CREDIT_CARD_NUMBER"),
    ("username", "USERNAME"),
    ("mail", "EMAIL_ADDRESS"),
]


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


def clasificationcolumns(listofcolumns, regex):
    """generate regex comparation"""
    listclasificated = []
    for column in listofcolumns:
        value = None
        for key in regex:
            busqueda = re.search(key[0], column)
            if busqueda is not None:
                value = (column, key[1])
                listclasificated.append(value)
        if value is None:
            value = (column, "N/A")
            listclasificated.append(value)
    return listclasificated


def clasificationdb(listofdatabases, cursor):
    """generate clasificatioDb"""

    response = []

    for database in listofdatabases:
        cursor.execute(f"USE {database}")
        tables = querymysql("show tables", cursor)

        for table in tables:
            columns = querymysql(f"show columns from {table}", cursor)
            columnsclasification = clasificationcolumns(columns, keywords)

            tables_column = (database, table, columnsclasification)
            response.append(tables_column)

    return response
