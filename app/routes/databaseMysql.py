from fastapi import APIRouter
from app.models.database import DataBase
from app.functions.databaseMysql import connection_db


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
    connectionMysql = connection_db(database.host, database.User, database.Password)
    connectionMysql.execute("SHOW DATABASES")
    for databases in connectionMysql:
        Datas.append(databases)

    return Datas
