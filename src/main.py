from fastapi import FastAPI, HTTPException, Query, status
from models import ShoppingItem, Category
from database import db

app = FastAPI(title = "Fast Shopping List API", version = "1.0.0")

@app.get("/items", response_model=list[ShoppingItem])
async def get_items(category: Category | None = None):
    """Retrieve all shopping items, optionally filtered by category."""
    return db.get_all(category)

@app.post("/items", status_code= status.HTTP_201_CREATED, response_model=ShoppingItem)
async def add_item(item: ShoppingItem):
    """Add a new item to the shopping list."""
    return db.add_item(item)

@app.patch("/items/{item_id}/quantity", response_model=ShoppingItem)
async def update_item_quantity(item_id: int,new_qty: int = Query(..., gt=0)):
    """Update the quantity of a specific shopping item by its ID."""
    try:
        return db.update_quantity(item_id, new_qty)
    except KeyError as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))
    
@app.delete("/items/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_item(item_id: int):
    """Delete a specific shopping item by its ID."""
    try:
        db.delete_item(item_id)
    except KeyError as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))
    
@app.delete("/items", status_code=status.HTTP_204_NO_CONTENT)
async def clear_items():
    """Clear all items from the shopping list."""
    db.clear_all()
    return None

@app.get("/", tags=["General"])
async def welcome_message():
    """
    Docstring for welcome_message
    
    Welcome message for the Fast Shopping List API.
    """

    return {
        "message": "Welcome to the Fast Shopping List API!",
        "docs": "/docs",
        "status": "Running"
    }