from fastapi import FastAPI
from app.config.db import Database

app = FastAPI()

@app.on_event("startup")
async def start_db():
    await Database.connect()

@app.on_event("shutdown")
async def shutdown_db():
    await Database.disconnect()

@app.get("/")
async def root():
    return {"message": "MongoDB connection ready!"}
