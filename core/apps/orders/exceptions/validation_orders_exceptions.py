from dataclasses import dataclass

from core.apps.orders.config.order_config import (
    NAME_RECEIVER_NOT_ALPHABETIC,
    NOT_ALLOWED_SPECIAL_SYMBOLS_IN_DELIVERY_ADDERSS,
    NOT_CORRECT_DOMAIN_EMAIL,
    NOT_CORRECT_FROMAT_EMAIL,
    PHONE_NUMBER_CONTAINS_NOT_ONLY_DIGITS,
    PHONE_NUMBER_CONTAINS_SOME_STRANGE_SYMBOLS,
    SOME_WHITESPACE_IN_ORDER,
    TOO_MUCH_LENGTH_NAME_RECEIVER,
)
from core.apps.orders.exceptions.base_order_exception import BaseExceptionOrder


@dataclass(frozen=True)
class TooMuchLengthNameReceiverException(BaseExceptionOrder):
    @property
    def message(self):
        return f"{TOO_MUCH_LENGTH_NAME_RECEIVER}"


@dataclass(frozen=True)
class SomeOrderDataIsEmptyException(BaseExceptionOrder):
    @property
    def message(self):
        return f"{SOME_WHITESPACE_IN_ORDER}"


@dataclass(frozen=True)
class IsNameReceiverNotAlphabeticSpecException(BaseExceptionOrder):
    @property
    def message(self):
        return f"{NAME_RECEIVER_NOT_ALPHABETIC}"


# phone number  noqa
@dataclass(frozen=True)
class PhoneNumberContainsNotOnlyDigitsException(BaseExceptionOrder):
    @property
    def message(self):
        return f"{PHONE_NUMBER_CONTAINS_NOT_ONLY_DIGITS}"


@dataclass(frozen=True)
class PhoneNumberContainsNotAllowedSymblosException(BaseExceptionOrder):
    @property
    def message(self):
        return f"{PHONE_NUMBER_CONTAINS_SOME_STRANGE_SYMBOLS}"


# delivery address
@dataclass(frozen=True)
class DeliveryAddressNotAllowedSymbolsException(BaseExceptionOrder):
    @property
    def message(self):
        return f"{NOT_ALLOWED_SPECIAL_SYMBOLS_IN_DELIVERY_ADDERSS}"


# email
@dataclass(frozen=True)
class IncorrectDomainEmailException(BaseExceptionOrder):
    @property
    def message(self):
        return f"{NOT_CORRECT_DOMAIN_EMAIL}"


@dataclass(frozen=True)
class IncorrectFormatEmailException(BaseExceptionOrder):
    @property
    def message(self):
        return f"{NOT_CORRECT_FROMAT_EMAIL}"
