from fastapi import APIRouter, HTTPException, Query, status

from controllers.items_controller import (
    create_item,
    get_item,
    latest_item,
    list_items,
)
from responses.base_response import ApiResponse, ok
from schemas.itemSchemas import ItemCreate, ItemRead

router = APIRouter(prefix="/items", tags=["Items"])


@router.post(
    "/",
    status_code=status.HTTP_201_CREATED,
    response_model=ApiResponse[ItemRead],
)
def add_item(new_item: ItemCreate):
    created_item = create_item(new_item)
    return ok(created_item, message="Item created successfully")


@router.get("/", response_model=ApiResponse[list[ItemRead]])
def list_items_route(
    limit: int = Query(default=100, ge=1, le=100),
    offset: int = Query(default=0, ge=0),
):
    return ok(list_items(limit=limit, offset=offset))


@router.get("/latest/", response_model=ApiResponse[ItemRead])
def get_latest_item():
    latest = latest_item()
    if latest is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="No items found",
        )
    return ok(latest)


@router.get("/{item_id}/", response_model=ApiResponse[ItemRead])
def get_item_by_id(item_id: int):
    item = get_item(item_id)
    if item is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Item with id {item_id} not found",
        )
    return ok(item)
