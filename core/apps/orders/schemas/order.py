from decimal import Decimal
from typing import (
    Any,
    List,
)

from pydantic.dataclasses import dataclass


@dataclass
class OrderProductItemSchema:
    product_id: int
    quantity: int


@dataclass
class OrderSchema:
    user: Any
    name_receiver: str
    phone_number: str
    order_items: List[OrderProductItemSchema]
    delivery_address: str
    email: str
    total_price: Decimal
    required_delivery: bool = True
    payment_on_get: bool = True

    class Config:
        max_anystr_length = 60
        anystr_strip_whitespace = True


@dataclass
class OrderItemsResponseSchema:
    product: int
    title: str
    price: Decimal
    quantity: int


@dataclass
class OrderItemsSchema:
    items: List[OrderItemsResponseSchema]


@dataclass
class ValidateProductsQuantityId:
    list_of_product_quntity_and_ids: List[OrderProductItemSchema]
