from dataclasses import dataclass

from core.apps.orders.config.order_config import (
    BASE_EXCEPTION_ORDERS,
    COULD_NOT_CREATE_ORDER_ITEM,
    INSUFFICIENT_QUANTITY,
    PRODUCT_NOT_FOUND_EXCEPTION,
)


@dataclass
class BaseExceptionOrder(Exception):
    product: int = None

    @property
    def message(self):
        return BASE_EXCEPTION_ORDERS


@dataclass
class NotEnoughQuantityProducts(BaseExceptionOrder):
    @property
    def message(self):
        return f"{INSUFFICIENT_QUANTITY.format(product_id=self.product)}"


@dataclass
class NotFoundProductException(BaseExceptionOrder):
    @property
    def message(self):
        return f"{PRODUCT_NOT_FOUND_EXCEPTION.format(product_id=self.product)}"


@dataclass
class OrderItemsCreationException(BaseExceptionOrder):
    @property
    def message(self):
        return f"{COULD_NOT_CREATE_ORDER_ITEM}"
