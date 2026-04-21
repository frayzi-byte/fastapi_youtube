from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.schemas.item_schema import (
    CreateItem,
    ItemUpdate,
    ItemResponse
)
from app.repositories.items_repository import (
    create_item,
    get_items,
    get_item_by_id,
    update_item,
    delete_item
)

router = APIRouter(prefix="/items", tags=["Items"])

@router.post("/", response_model=ItemResponse)
def create_new_item(item : CreateItem, db : Session = Depends(get_db)):
    return create_item(db, item)

@router.get("/", response_model=list[ItemResponse])
def list_items(db: Session = Depends(get_db)):
    return get_items(db)

@router.get("/{item_id}", response_model=ItemResponse)
def item_by_id(item_id : int, db : Session = Depends(get_db)):
    item = get_item_by_id(db, item_id)    
    if not item :
        raise HTTPException(status_code=404, detail="Item not found!")
    return item

@router.put("/{item_id}", response_model=ItemResponse)
def edit_item(item_id : int, item : ItemUpdate, db : Session = Depends(get_db)):
    updated_item = update_item(db, item_id, item)
    if not updated_item:
        raise HTTPException(status_code=404, detail="Item not found!")
    return updated_item

@router.delete("/{item_id}", response_model=ItemResponse)
def remove_item(item_id : int, db : Session = Depends(get_db)):
    deleted_item = delete_item(db, item_id)
    if not deleted_item:
        raise HTTPException(status_code=404, detail="Item not found!")
    return deleted_item