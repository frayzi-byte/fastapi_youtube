from sqlalchemy.orm import Session
from models.item_model import Item
from schemas.item_schema import CreateItem, ItemUpdate

def create_item(db : Session, item : CreateItem):
    db_item = Item(
        body = item.body
    )
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

def get_items(db : Session):
    return db.query(Item).all()

