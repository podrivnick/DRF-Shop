from dataclasses import dataclass

from core.apps.orders.config.order_config import (
    NAME_RECEIVER_IS_EMPTY,
    NAME_RECEIVER_NOT_ALPHABETIC,
    PHONE_NUMBER_CONTAINS_NOT_ONLY_DIGITS,
    PHONE_NUMBER_CONTAINS_SOME_STRANGE_SYMBOLS,
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


# phone number  noqa
@dataclass(frozen=True)
class PhoneNumberContainsNotOnlyDigits(BaseExceptionOrder):
    @property
    def message(self):
        return f"{PHONE_NUMBER_CONTAINS_NOT_ONLY_DIGITS}"


@dataclass(frozen=True)
class PhoneNumberContainsNotAllowedSymblos(BaseExceptionOrder):
    @property
    def message(self):
        return f"{PHONE_NUMBER_CONTAINS_SOME_STRANGE_SYMBOLS}"
