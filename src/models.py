from pydantic import BaseModel, Field
from enum import Enum
from typing import Optional

class Category(str, Enum):
    DAIRY = "dairy products"
    DRY = "dry products"
    VEGGIES = "fruits and vegetables"
    BUTCHER = "butcher products"

class ShoppingItem(BaseModel):
    id: Optional[int] = None
    name: str = Field(..., min_length=2)
    category: Category
    quantity: int = Field(1, gt=0)
    is_bought: bool = False