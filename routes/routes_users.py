from schemas.userSchemas import CreateUser
from fastapi import APIRouter
from main import users

router = APIRouter(prefix="/users", tags=["Users"])

@router.post("/")
def create_user(user : CreateUser):
    return {
        "message" : "Success!",
        "email": user.email,
    }

@router.get("/")
def list_users():
    return users

@router.get("/latest_user/")
def get_latest_user():
    return users[-1]

@router.get("/{user_id}")
def get_user_by_id(user_id : int):
    for user in users:
        if user["id"] == user_id:
            return user