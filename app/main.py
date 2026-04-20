import uvicorn
from fastapi import FastAPI
from app.core.database import Base, engine
from app.routers.routers_items import router as items_router

app = FastAPI()
app.include_router(items_router)

Base.metadata.create_all(bind=engine)

@app.get("/")
def hello_world():
    return {"message" : "Hello world!"}

if __name__ == "__main__":
    uvicorn.run(app, reload=True)