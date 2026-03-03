from typing import Annotated
from fastapi import APIRouter, Path
from main import items
from schemas.itemSchemas import CreateItem

router = APIRouter(prefix="/items", tags=["Items"])

@router.add("/")
def add_item(new_item : CreateItem):
    return {
        "message" : "Success!",
        "id": new_item.id,
    }

@router.get("/")
def list_items():
    return items

@router.get("/latest/")
def get_latest_item():
    return items[-1]

@router.get("/{item_id}/")
def get_item_by_id(item_id : int):
    for item in items:
        if item["id"] == item_id:
            return {item}