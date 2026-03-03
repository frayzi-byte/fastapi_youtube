from typing import Annotated
from fastapi import FastAPI, Body, Path
from pydantic import BaseModel, EmailStr

import uvicorn

from routes.routes_items import router as items_router
from routes.routes_users import router as users_router

app = FastAPI()
app.include_router(items_router)
app.include_router(users_router)

items = [
    {
        "id" : 1,
        "body" : "This is a test item No 1",},
    {
        "id" : 2,
        "body" : "This is a test item No 2",},
]

users = [
    {
        "id" : 1,
        "username" : "puffaball14",
        "email" : "puffabal@gmail.com",
    },
    {
        "id" : 2,
        "username" : "puffaballhater15",
        "email" : "ihatepuffaball@gmail.com",
    },]

@app.get("/")
def hello_world():
    return {"message" : "Hello world!"}

if __name__ == "__main__":
    uvicorn.run(app, reload=True)