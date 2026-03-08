from schemas.itemSchemas import ItemCreate, ItemRead
from services.items_service import ItemsService

service = ItemsService()


def create_item(new_item: ItemCreate) -> ItemRead:
    return service.create_item(new_item)


def list_items(limit: int, offset: int) -> list[ItemRead]:
    return service.list_items(limit=limit, offset=offset)


def latest_item() -> ItemRead | None:
    return service.latest_item()


def get_item(item_id: int) -> ItemRead | None:
    return service.get_item(item_id)
