from typing import Annotated
from fastapi import FastAPI, Body, Path
from pydantic import BaseModel, EmailStr
import sqlite3

import uvicorn

conn = sqlite3.connect("database.db")
cursor = conn.cursor()

from routes.routes_items import router as items_router

app = FastAPI()
app.include_router(items_router)

@app.get("/")
def hello_world():
    return {"message" : "Hello world!"}

if __name__ == "__main__":
    uvicorn.run(app, reload=True)