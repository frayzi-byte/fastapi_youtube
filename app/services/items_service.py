from app.repositories.items_repository import get_item_by_id, get_items, create_item, update_item, delete_item
from fastapi import HTTPException

def get_item_by_id_service(db, item_id: int):

    item = get_item_by_id(db, item_id)

    if not item :
        raise HTTPException(status_code=404, detail="Item not found!")
    
    return item

def get_all_items_service(db):

    item = get_items(db)

    return item

def post_items_service(db, new_item):

    if not new_item.name.strip() or new_item.name == "string":
        raise HTTPException(status_code=400, detail="Name is required")
    
    result_from_db = create_item(db, new_item)

    return result_from_db

def change_item_service(db, item_id, item_data):

    if not item_id.name.strip() or item_id.name == "string":
        raise HTTPException(status_code=400, detail="Name is required")
    
    result_from_db = update_item(db, item_id, item_data)

    return result_from_db

def remove_item_service(db, item_id):

    if item_id == None:
        raise HTTPException(status_code=404, detail="Item not found")
    
    result_from_db = delete_item(db, item_id)

    return result_from_db