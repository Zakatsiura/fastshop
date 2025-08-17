from enum import Enum
from sqladmin import ModelView
from typing import List
from sqlmodel import Field
from src.basket.models.databse import Basket, BasketItem
from src.users.models.database import User

# Категорія для адмін-панелі
ADMIN_CATEGORY = 'Shop'

# Enum для статусу кошика
class BasketStatus(str, Enum):
    OPEN = 'Open'
    CLOSED = 'Closed'
    CANCELLED = 'Cancelled'

# Адмін для Basket
class BasketAdmin(ModelView, model=Basket):
    column_list = [Basket.id, Basket.user_id, Basket.status, Basket.created_at, Basket.updated_at]
    column_searchable_list = [Basket.user_id]
    column_filters = [Basket.status]
    icon = 'fa-solid fa-shopping-basket'
    category = ADMIN_CATEGORY

# Адмін для BasketItem
class BasketItemAdmin(ModelView, model=BasketItem):
    column_list = [BasketItem.id, BasketItem.basket_id, BasketItem.product_id, BasketItem.quantity, BasketItem.price]
    column_searchable_list = [BasketItem.product_id]
    icon = 'fa-solid fa-box'
    category = ADMIN_CATEGORY

# Функція для реєстрації адмін-панелей
def register_basket_admin_views(admin):
    admin.add_view(BasketAdmin)
    admin.add_view(BasketItemAdmin)
