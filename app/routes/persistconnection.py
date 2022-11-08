from fastapi import APIRouter
from app.models.database import DataBase
from app.functions.databaseMysql import connection_dbMysql
from app.functions.databaseMongo import connection_dbMongo
from app.models.env import mongoenv, keyencriptor
from app.functions.encryptor import encrypt


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

    connectionMysql = connection_dbMysql(
        database.host, database.User, database.Password
    )
    connectionMysql.close()

    conectionMongo = connection_dbMongo(mongoenv.url, mongoenv.user, mongoenv.passw)

    user_encrypt = encrypt(database.User, keyencriptor.key)
    pass_encrypt = encrypt(database.Password, keyencriptor.key)

    format_value = {
        "user": f"{user_encrypt}",
        "pass": f"{pass_encrypt}",
        "url": f"{database.host}",
    }

    databasemongo = conectionMongo["meli"]
    mongotable = databasemongo["sqlcredentials"]
    insert_value = mongotable.insert_one(format_value)
    id_mongo = insert_value.inserted_id
    conectionMongo.close()
    return {"The credentials are saved correct with id: ": f"{id_mongo}"}
