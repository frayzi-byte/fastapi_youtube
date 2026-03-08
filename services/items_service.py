from repositories.items_repository import ItemsRepository
from schemas.itemSchemas import ItemCreate


class ItemsService:
    def __init__(self, repository: ItemsRepository | None = None) -> None:
        self.repository = repository or ItemsRepository()

    def create_item(self, item: ItemCreate) -> dict:
        return self.repository.add(body=item.body)

    def list_items(self, limit: int = 100, offset: int = 0) -> list[dict]:
        return self.repository.list_all(limit=limit, offset=offset)

    def latest_item(self) -> dict | None:
        return self.repository.get_latest()

    def get_item(self, item_id: int) -> dict | None:
        return self.repository.get_by_id(item_id)
