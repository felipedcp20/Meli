from fastapi import APIRouter , HTTPException
import bson
from bson.objectid import ObjectId
from app.models.env import mongoenv
from app.functions.databaseMongo import connection_dbMongo



router = APIRouter()


@router.get(path="/api/v1/database/scan/", status_code=201)
async def getclasification(iddatabase):
    """_summary_

    Args:
        iddatabase (str): Id Database to consult clasification

    Returns:
        json: json clasification database
    """
    if not bson.ObjectId.is_valid(iddatabase):
        raise HTTPException(400, "Invalid id")

    conectionMongo = connection_dbMongo(mongoenv.url, mongoenv.user, mongoenv.passw)

    databasemongo = conectionMongo["meli"]
    mongotable = databasemongo["SqlClasification"]
    objectid = {"_id": ObjectId(iddatabase)}

    elementfind = mongotable.find_one(objectid)
    if elementfind is None:
        raise HTTPException(status_code=400, detail="Invalid Id")

    return {"conusult": f"{elementfind}"}
