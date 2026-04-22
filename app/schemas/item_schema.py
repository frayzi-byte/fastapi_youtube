from pydantic import BaseModel
from typing import Optional

class CreateItem(BaseModel):
    name : str
    description: Optional[str] = None

class ItemUpdate(BaseModel):
    name : str
    description: Optional[str] = None

class ItemResponse(BaseModel):
    id : int
    name : str
    description: Optional[str] = None

    class Config:
        from_attributes = True