from typing import Generic, TypeVar

from pydantic import BaseModel

T = TypeVar("T")


class ApiResponse(BaseModel, Generic[T]):
    success: bool = True
    message: str = "Success"
    data: T | None = None


def ok(data=None, message: str = "Success") -> dict:
    return ApiResponse(message=message, data=data).model_dump()
