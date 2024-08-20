from dataclasses import (
    dataclass,
    field,
)
from decimal import Decimal
from typing import (
    Any,
    List,
)


@dataclass(eq=False)
class OrderProductItemSchema:
    product_id: int
    quantity: int


@dataclass(eq=False)
class OrderSchema:
    user: Any
    name_receiver: str
    phone_number: str
    order_items: List[OrderProductItemSchema] = field(default_factory=list, kw_only=True)
    delivery_address: str
    email: str
    total_price: Decimal
    required_delivery: bool = field(default=True)
    payment_on_get: bool = field(default=True)

    def __post_init__(self):
        self.name_receiver = self.validate_and_strip_string(self.name_receiver, self.Config.str_max_length)

    @staticmethod
    def validate_and_strip_string(value: str, max_length: int) -> str:
        value = value.strip()
        if len(value) > max_length:
            raise ValueError(f"String length exceeds {max_length} characters")
        return value

    class Config:
        str_max_length = 60
        str_strip_whitespace = True


@dataclass(eq=False)
class ValidateProductsQuantityId:
    list_of_product_quntity_and_ids: List[OrderProductItemSchema] = field(default_factory=list, kw_only=True)


@dataclass
class OrderItemsResponseSchema:
    product: int
    title: str
    price: Decimal
    quantity: int
    discount: Decimal = field(default=Decimal(0))


@dataclass
class OrderItemsSchema:
    items: List[OrderItemsResponseSchema] = field(default_factory=list, kw_only=True)

    def __eq__(self, other):
        if not isinstance(other, OrderItemsSchema):
            return False
        return self.items == other.items
