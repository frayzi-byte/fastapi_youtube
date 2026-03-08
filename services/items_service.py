from repositories.items_repository import ItemsRepository
from schemas.itemSchemas import CreateItem


class ItemsService:
    def __init__(self, repository: ItemsRepository | None = None) -> None:
        self.repository = repository or ItemsRepository()

    def create_item(self, item: CreateItem) -> dict:
        return self.repository.add(item.dict())

    def list_items(self) -> list:
        return self.repository.list_all()

    def latest_item(self) -> dict | None:
        return self.repository.get_latest()

    def get_item(self, item_id: int) -> dict | None:
        return self.repository.get_by_id(item_id)
