from fastapi import FastAPI
from fastapi import APIRouter
from app.routes import persistconnection
from app.routes import clasification

app = FastAPI()


@app.get("/")
async def root():
    """service"""
    return {"service": "Meli", "version": "1.0"}


api_router = APIRouter()

api_router.include_router(persistconnection.router, tags=["databaseMysql"])
api_router.include_router(clasification.router, tags=["clasification"])

app.include_router(api_router)
