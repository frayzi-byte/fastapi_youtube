from schemas.userSchemas import CreateUser
from fastapi import APIRouter

router = APIRouter(prefix="/users", tags=["Users"])

@router.post("/")
def create_user(user : CreateUser):
    return {
        "message" : "Success!",
        "email": user.email,
    }

@router.get("/")
def ping_user():
    return {
        "ok" : True
    }