from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    """service"""
    return {"service": "Meli", "version": "1.0"}
