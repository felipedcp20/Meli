from fastapi import FastAPI , APIRouter
from fastapi.staticfiles import StaticFiles
from app.routes import persistconnection
from app.routes import clasification
from app.routes import getclasification
from app.routes import view


app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/")
async def root():
    """service"""
    return {"service": "Meli", "version": "1.0"}


api_router = APIRouter()

api_router.include_router(persistconnection.router, tags=["databaseMysql"])
api_router.include_router(clasification.router, tags=["clasification"])
api_router.include_router(getclasification.router, tags=["getclasification"])
api_router.include_router(view.router)

app.include_router(api_router)
