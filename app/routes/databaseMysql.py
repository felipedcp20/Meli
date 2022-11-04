from fastapi import APIRouter
from app.models.database import DataBase
from app.functions.databaseMysql import connection_db


router = APIRouter()

@router.post(path="/api/v1/database")
async def databasepersistence(database : DataBase):
    """_summary_

    Args:
        database (DataBase): _description_

    Returns:
        _type_: _description_
    """

    status = connection_db(database.host,database.User,database.Password)
    print(status)
    return {"message"}
