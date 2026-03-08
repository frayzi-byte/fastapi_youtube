from contextlib import asynccontextmanager

from fastapi import FastAPI
import uvicorn

from routes.items_routes import router as items_router
from database.connection import init_db


@asynccontextmanager
async def lifespan(_: FastAPI):
    init_db()
    yield


app = FastAPI(
    title="Items API",
    version="1.0.0",
    lifespan=lifespan,
)
app.include_router(items_router)


@app.get("/")
def healthcheck() -> dict[str, str]:
    return {"message": "Items API is running"}


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000)
