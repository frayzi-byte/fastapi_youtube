from fastapi import APIRouter
from schemas.itemSchemas import CreateItem
from services.items_service import ItemsService
from responses.base_response import ok

router = APIRouter(prefix="/items", tags=["Items"])
service = ItemsService()


@router.post("/")
def add_item(new_item: CreateItem):
    created_item = service.create_item(new_item)
    return ok(created_item)


@router.get("/")
def list_items():
    return ok(service.list_items())


@router.get("/latest/")
def get_latest_item():
    return ok(service.latest_item())


@router.get("/{item_id}/")
def get_item_by_id(item_id: int):
    return ok(service.get_item(item_id))
