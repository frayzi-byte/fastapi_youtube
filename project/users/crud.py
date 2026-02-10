from schemas.userSchemas import CreateUser

def create_user(user_in : CreateUser):
    return {
        "success": True,
        "user": user_in,
    }

def ping_user():
    return {
        "ok" : True
    }