import re
from dataclasses import (
    dataclass,
    field,
)
from typing import Pattern

from core.apps.orders.exceptions.validation_orders_exceptions import (
    DeliveryAddressNotAllowedSymbolsException,
    IncorrectDomainEmailException,
    IncorrectFormatEmailException,
    IsNameReceiverNotAlphabeticSpecException,
    PhoneNumberContainsNotAllowedSymblosException,
    SomeOrderDataIsEmptyException,
    TooMuchLengthNameReceiverException,
)
from core.apps.orders.utils.base_spec import Specification


# max length  noqa
@dataclass(frozen=True)
class MaxLengthSpec(Specification):
    max_length: int = field(default=60)

    def is_satisfied(
        self,
        item: str,
    ) -> bool:
        if len(item) > self.max_length:
            raise TooMuchLengthNameReceiverException()
        return True


# not empty  noqa
@dataclass(frozen=True)
class IsNotEmptySpec(Specification):
    def is_satisfied(
        self,
        item: str,
    ) -> bool:
        if not bool(item.strip()):
            raise SomeOrderDataIsEmptyException()
        return True


# only alpha  noqa
@dataclass(frozen=True)
class IsAlphabeticSpec(Specification):
    def is_satisfied(
        self,
        item: str,
    ) -> bool:
        if not item.replace(" ", "").isalpha():
            raise IsNameReceiverNotAlphabeticSpecException()
        return True


# Spec for check phone number for symblols  noqa
@dataclass(frozen=True)
class AllowedCharactersSpec(Specification):
    _allowed_chars: str = field(default="+-")
    _phone_pattern: Pattern[str] = field(default_factory=lambda: re.compile(r"^\+?\d{1,3}[\s.-]?\(?\d{1,4}?\)?[\s.-]?\d{1,4}[\s.-]?\d{1,4}[\s.-]?\d{1,9}$"))

    def is_satisfied(
        self,
        item: str,
    ) -> bool:
        for char in item:
            if not (char.isdigit() or char in self._allowed_chars or char.isspace()):
                raise PhoneNumberContainsNotAllowedSymblosException()

        # Проверка на соответствие шаблону
        if not self._phone_pattern.match(item):
            raise PhoneNumberContainsNotAllowedSymblosException()
        return True


# Spec for delivery address  noqa
@dataclass(frozen=True)
class NoSpecialCharactersSpec(Specification):
    _forbidden_chars: str = field(default="!@#$%^&*()[]{};:'\"<>?\\|`~")

    def is_satisfied(
        self,
        item: str,
    ) -> bool:
        if any(char in self._forbidden_chars for char in item):
            raise DeliveryAddressNotAllowedSymbolsException()
        return True


# Spec for email   noqa
@dataclass(frozen=True)
class ValidDomainSpec(Specification):
    _domain_pattern: Pattern[str] = field(default=re.compile(r"@[a-zA-Z0-9-]+\.[a-zA-Z]{2,}$"))

    def is_satisfied(
        self,
        item: str,
    ) -> bool:
        if not re.search(
            self._domain_pattern,
            item,
        ):
            raise IncorrectDomainEmailException()
        return True


@dataclass(frozen=True)
class ValidEmailSpec(Specification):
    _email_pattern: Pattern[str] = field(default_factory=lambda: re.compile(r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"))

    def is_satisfied(
        self,
        item: str,
    ) -> bool:
        if not re.match(
            self._email_pattern,
            item,
        ):
            raise IncorrectFormatEmailException()
        return True
