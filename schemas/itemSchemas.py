from pydantic import BaseModel, EmailStr, Field

class CreateItem(BaseModel):
    id: int
    name: str = Field(min_length=5, max_length=30)