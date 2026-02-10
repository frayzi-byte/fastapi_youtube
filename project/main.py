from typing import Annotated
from fastapi import FastAPI, Body, Path
from pydantic import BaseModel, EmailStr

import uvicorn

from items.views import router as items_router
from users.views import router as users_router

app = FastAPI()
app.include_router(items_router)
app.include_router(users_router)

class CreateUser(BaseModel):
    email : EmailStr

@app.get("/")
def hello_world():
    return {"message" : "Hello world!"}

if __name__ == "__main__":
    uvicorn.run(app, reload=True)