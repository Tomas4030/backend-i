from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import logging

logging.basicConfig(level=logging.INFO,format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)

app = FastAPI()

_items_ = []

class Item(BaseModel):
    name: str
    price: float


@app.get("/")
async def read_root():
    logger.info("Root endpoint called")
    return {"message": "Welcome to the FastAPI API!"}


@app.post("/items/")
async def create_item(item: Item):
    if not item.name or not item.price:
        raise HTTPException(
            status_code=400, detail="Item must have a name and price")

    _items_.append(item)
    logger.info(f"Item created: {item}")
    return {"item": item}


@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    if item_id >= len(_items_) or item_id < 0:
        logger.error(f"Item with ID {item_id} not found.")
        raise HTTPException(status_code=404, detail="Item not found")

    _items_[item_id] = item
    logger.info(
        f"Item with ID {item_id} updated successfully. New data: {item}")

    return {"item": item}


@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    if item_id >= len(_items_) or item_id < 0:
        logger.error(f"Item with ID {item_id} not found.")
        raise HTTPException(status_code=404, detail="Item not found")

    deleted_item = _items_.pop(item_id)
    logger.info(f"Item with ID {item_id} deleted. Item: {deleted_item}")

    return {"message": f"Item with ID {item_id} has been deleted."}
