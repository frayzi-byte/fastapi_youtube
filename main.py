from typing import Annotated
from fastapi import FastAPI, Body, Path
from pydantic import BaseModel, EmailStr
from fastapi import FastAPI
from core.database import Base, engine
from routers.routers_items import router as product_router

import uvicorn
from routers.routers_items import router as items_router

app = FastAPI()
app.include_router(items_router)

Base.metadata.create_all(bind=engine)

@app.get("/")
def hello_world():
    return {"message" : "Hello world!"}

if __name__ == "__main__":
    uvicorn.run(app, reload=True)