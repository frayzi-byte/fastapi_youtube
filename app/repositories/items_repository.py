from sqlalchemy.orm import Session
from app.models.item_model import Item
from app.schemas.item_schema import CreateItem, ItemUpdate

def create_item(db : Session, item : CreateItem):
    db_item = Item(
        name = item.name,
        description = item.description,
    )
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

def get_items(db : Session):
    return db.query(Item).all()

def get_item_by_id(db : Session, item_id : int):
    return db.query(Item).filter(Item.id == item_id).first()

def update_item(db : Session, item_id : int, item_data : ItemUpdate):
    item = db.query(Item).filter(Item.id == item_id).first()
    if not item:
        return None
    
    item.name = item_data.name
    item.description = item_data.description

    db.commit()
    db.refresh(item)
    return item

def delete_item(db : Session, item_id : int):
    item = db.query(Item).filter(Item.id == item_id).first()
    if not item : 
        return None
    
    db.delete(item)
    db.commit()
    return item