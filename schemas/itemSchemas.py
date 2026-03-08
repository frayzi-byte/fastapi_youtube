from pydantic import BaseModel, Field

class CreateItem(BaseModel):
    id: int
    body: str = Field(min_length=5, max_length=30)