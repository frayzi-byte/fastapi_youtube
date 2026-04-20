from pydantic import BaseModel, EmailStr, Field

class CreateItem(BaseModel):
    id: int
    body: str

class ItemUpdate(BaseModel):
    id : int
    body : str

class ItemResponse(BaseModel):
    id : int
    body : str

    class Config:
        from_attributes = True