from fastapi import FastAPI
from fastapi import APIRouter

app = FastAPI()


@app.get("/")
async def root():
    """service"""
    return {"service": "Meli", "version": "1.0"}


apirouter = APIRouter
