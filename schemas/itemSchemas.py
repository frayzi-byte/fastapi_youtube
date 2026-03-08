from datetime import datetime

from pydantic import BaseModel, Field, field_validator


class ItemCreate(BaseModel):
    body: str = Field(min_length=5, max_length=280)

    @field_validator("body")
    @classmethod
    def clean_body(cls, value: str) -> str:
        clean_value = value.strip()
        if len(clean_value) < 5:
            raise ValueError("body must have at least 5 non-space characters")
        return clean_value


class ItemRead(BaseModel):
    id: int
    body: str
    created_at: datetime
