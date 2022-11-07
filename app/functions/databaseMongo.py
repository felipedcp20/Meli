from pymongo import MongoClient
from fastapi import HTTPException


def connection_dbMongo(url, username, password):
    """_summary_

    Args:
        url (str): _description_
        username (str): _description_
        password (str): _description_

    Returns:
        _type_: _description_
    """

    url = url.replace("<user>", username).replace("<password>", password)

    client = MongoClient(url)

    try:
        client.server_info()
    except Exception as error:
        detail = f"connection to sql: ok , please consult the mongoAcces {error}"
        raise HTTPException(status_code=404, detail=detail) from error

    return client
