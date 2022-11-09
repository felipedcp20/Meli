import bson
from bson.objectid import ObjectId
from fastapi import APIRouter , HTTPException
from fastapi import Request

from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from app.functions.databaseMongo import connection_dbMongo
from app.models.env import mongoenv



router = APIRouter()


templates = Jinja2Templates(directory="app/templates")


@router.get("/view", response_class=HTMLResponse)
async def View_Html(request: Request, iddatabase: str):
    """Return View in Html"""
    if not bson.ObjectId.is_valid(iddatabase):
        raise HTTPException(400, "Invalid id")

    conectionMongo = connection_dbMongo(mongoenv.url, mongoenv.user, mongoenv.passw)

    databasemongo = conectionMongo["meli"]
    mongotable = databasemongo["SqlClasification"]
    objectid = {"_id": ObjectId(iddatabase)}

    elementfind = mongotable.find_one(objectid)
    if elementfind is None:
        raise HTTPException(status_code=400, detail="Invalid Id")


    return templates.TemplateResponse("index.html", {"request": request, "front": elementfind})
