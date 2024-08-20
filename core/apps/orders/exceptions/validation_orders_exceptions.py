from dataclasses import dataclass

from core.apps.orders.config.order_config import (
    NAME_RECEIVER_IS_EMPTY,
    NAME_RECEIVER_NOT_ALPHABETIC,
    TOO_MUCH_LENGTH_NAME_RECEIVER,
)
from core.apps.orders.exceptions.base_order_exception import BaseExceptionOrder


@dataclass(frozen=True)
class TooMuchLengthNameReceiver(BaseExceptionOrder):
    @property
    def message(self):
        return f"{TOO_MUCH_LENGTH_NAME_RECEIVER}"


@dataclass(frozen=True)
class NameReceiverIsEmpty(BaseExceptionOrder):
    @property
    def message(self):
        return f"{NAME_RECEIVER_IS_EMPTY}"


@dataclass(frozen=True)
class IsNameReceiverNotAlphabeticSpec(BaseExceptionOrder):
    @property
    def message(self):
        return f"{NAME_RECEIVER_NOT_ALPHABETIC}"
