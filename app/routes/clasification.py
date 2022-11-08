from datetime import datetime
import bson
from bson.objectid import ObjectId
from fastapi import APIRouter, HTTPException


from app.models.env import mongoenv, keyencriptor
from app.functions.databaseMongo import connection_dbMongo
from app.functions.databaseMysql import connection_dbMysql, clasificationdb
from app.functions.encryptor import decrypt


router = APIRouter()
time = datetime.now()
date = time.strftime("%Y-%m-%d %H:%M%S")


@router.post(path="/api/v1/database/scan", status_code=201)
async def clasification(iddatabase):
    """_summary_

    Args:
        iddatabase (_type_): _description_

    Raises:
        HTTPException: _description_
        HTTPException: _description_

    Returns:
        _type_: _description_
    """
    if not bson.ObjectId.is_valid(iddatabase):
        raise HTTPException(400, "Invalid id")

    conectionMongo = connection_dbMongo(mongoenv.url, mongoenv.user, mongoenv.passw)

    databasemongo = conectionMongo["meli"]
    mongotable = databasemongo["sqlcredentials"]
    objectid = {"_id": ObjectId(iddatabase)}

    elementfind = mongotable.find_one(objectid)
    if elementfind is None:
        raise HTTPException(status_code=400, detail="Invalid Id")

    passw_decrypt = decrypt(
        elementfind["pass"].replace("b'", "").replace("'", ""), keyencriptor.key
    )
    user_decrypt = decrypt(
        elementfind["user"].replace("b'", "").replace("'", ""), keyencriptor.key
    )
    host = elementfind["url"]

    cursor = connection_dbMysql(host, user_decrypt, passw_decrypt)
    cursor.execute("SHOW DATABASES")

    databases = []

    for database in cursor:
        converttupla = "".join(map(str, database))
        databases.append(converttupla)

    databases.remove("information_schema")
    databases.remove("mysql")
    databases.remove("performance_schema")
    databases.remove("sys")
    values = {"clasificated": clasificationdb(databases, cursor), "date": date}


    mongotable = databasemongo["SqlClasification"]
    id_value = mongotable.insert_one(values).inserted_id


    return {"id of mysql clasificated": f"{id_value}"}
