from dataclasses import (
    dataclass,
    field,
)

from core.apps.orders.exceptions.validation_orders_exceptions import (
    IsNameReceiverNotAlphabeticSpec,
    NameReceiverIsEmpty,
    PhoneNumberContainsNotAllowedSymblos,
    TooMuchLengthNameReceiver,
)
from core.apps.orders.utils.base_spec import Specification


# max length  noqa
@dataclass(frozen=True)
class MaxLengthSpec(Specification):
    max_length: int = field(default=60)

    def is_satisfied(self, item: str) -> bool:
        if len(item) > self.max_length:
            raise TooMuchLengthNameReceiver()
        return True


# not empty  noqa
@dataclass(frozen=True)
class IsNotEmptySpec(Specification):
    def is_satisfied(self, item: str) -> bool:
        if not bool(item.strip()):
            raise NameReceiverIsEmpty()
        return True


# only alpha  noqa
@dataclass(frozen=True)
class IsAlphabeticSpec(Specification):
    def is_satisfied(self, item: str) -> bool:
        if not item.replace(" ", "").isalpha():
            raise IsNameReceiverNotAlphabeticSpec()
        return True


# Spec for check phone number for symblols  noqa
@dataclass(frozen=True)
class AllowedCharactersSpec(Specification):
    _allowed_chars: str = field(default="+-")

    def is_satisfied(self, item: str) -> bool:
        cleaned_item = item.replace(" ", "").replace("-", "").replace("+", "")
        if not cleaned_item.isdigit():
            raise PhoneNumberContainsNotAllowedSymblos()
        return True
