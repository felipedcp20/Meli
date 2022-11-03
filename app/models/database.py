from pydantic import BaseModel


class DataBase(BaseModel):
    """Create ObjectDataBase"""

    host: str
    User: str
    Password: str
