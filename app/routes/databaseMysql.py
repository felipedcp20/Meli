from fastapi import APIRouter
from app.models.database import DataBase
from app.functions.databaseMysql import connection_dbMysql
from app.functions.databaseMongo import connection_dbMongo
from app.models.env import mongoenv


router = APIRouter()


@router.post(path="/api/v1/database", status_code=201)
async def databasepersistence(database: DataBase):
    """_summary_

    Args:
        database (DataBase):
         host: str
        User: str
        Password: str

    Returns:
        _type_: _description_
    """

    Datas = []
    connectionMysql = connection_dbMysql(
        database.host, database.User, database.Password
    )
    connectionMysql.execute("SHOW DATABASES")
    for databases in connectionMysql:
        Datas.append(databases)

    coneccionMongo = connection_dbMongo(mongoenv.url, mongoenv.user, mongoenv.passw)
    coneccionMongo.server_info()

    return Datas
