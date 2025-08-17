from sqlmodel import SQLModel, Field, Relationship
from typing import Optional, List
from datetime import datetime
from enum import Enum
from src.users.models.database import User

class BasketStatus(str, Enum):
    OPEN = "Open"
    CLOSED = "Closed"
    CANCELLED = "Cancelled"

class BasketItem(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    basket_id: int = Field(foreign_key="basket.id")
    product_id: int
    quantity: int = 1
    price: float

    basket: Optional["Basket"] = Relationship(back_populates="items")


class Basket(SQLModel, table=True):
    __tablename__ = "basket"
    id: Optional[int] = Field(default=None, primary_key=True)
    user_id: int = Field(foreign_key="users.id")
    status: BasketStatus = Field(default=BasketStatus.OPEN)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    items: List[BasketItem] = Relationship(back_populates="basket")
