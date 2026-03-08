from fastapi import FastAPI
import uvicorn

from controllers.items_controller import router as items_router
from database.connection import init_db

app = FastAPI()
app.include_router(items_router)


@app.on_event("startup")
def startup() -> None:
    init_db()

@app.get("/")
def hello_world():
    return {"message" : "Hello world!"}

if __name__ == "__main__":
    uvicorn.run(app, reload=True)