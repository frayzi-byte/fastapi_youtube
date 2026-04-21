from pydantic import BaseModel

class CreateItem(BaseModel):
    name : str
    description: str

class ItemUpdate(BaseModel):
    name : str
    description: str

class ItemResponse(BaseModel):
    id : int
    name : str
    description: str

    class Config:
        from_attributes = True