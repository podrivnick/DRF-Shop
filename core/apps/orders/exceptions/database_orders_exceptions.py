from dataclasses import dataclass

from core.apps.orders.config.order_config import (
    COULD_NOT_CREATE_ORDER_ITEM,
    INSUFFICIENT_QUANTITY,
    PRODUCT_NOT_FOUND_EXCEPTION,
)
from core.apps.orders.exceptions.base_order_exception import BaseExceptionOrder


@dataclass(frozen=True)
class NotEnoughQuantityProducts(BaseExceptionOrder):
    @property
    def message(self):
        return f"{INSUFFICIENT_QUANTITY.format(product_id=self.product)}"


@dataclass(frozen=True)
class NotFoundProductException(BaseExceptionOrder):
    @property
    def message(self):
        return f"{PRODUCT_NOT_FOUND_EXCEPTION.format(product_id=self.product)}"


@dataclass(frozen=True)
class OrderItemsCreationException(BaseExceptionOrder):
    @property
    def message(self):
        return f"{COULD_NOT_CREATE_ORDER_ITEM}"
