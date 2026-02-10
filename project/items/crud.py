from schemas.itemSchemas import CreateItem

def create_item(new_item : CreateItem):
    return {
        "message" : f"Item created succesfulyl! Id : {CreateItem.id}"
    }