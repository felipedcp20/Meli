import os
from dotenv import load_dotenv

load_dotenv()


class mongoenv:
    """
    env mongo
    """

    user = os.getenv("dm_mongo_username")
    passw = os.getenv("db_mongo_password")
    url = os.getenv("db_mongo_url")


class keyencriptor:
    """
    keyencriptor
    """

    key = os.getenv("key_encriptor")
