from dataclasses import dataclass

from core.apps.orders.config.order_config import BASE_EXCEPTION_ORDERS


@dataclass(frozen=True)
class BaseExceptionOrder(Exception):
    product: int = None

    @property
    def message(self):
        return BASE_EXCEPTION_ORDERS
