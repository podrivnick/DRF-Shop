from abc import (
    ABC,
    abstractmethod,
)
from dataclasses import dataclass
from typing import (
    Any,
    Tuple,
)

from core.apps.orders.exceptions.validation_orders_exceptions import PhoneNumberContainsNotOnlyDigitsException


@dataclass(frozen=True)
class Specification(ABC):
    @abstractmethod
    def is_satisfied(
        self,
        item: Any,
    ) -> bool:
        pass

    def and_spec(
        self,
        other: 'Specification',
    ) -> 'AndSpecification':
        return AndSpecification((self, other))


@dataclass(frozen=True)
class AndSpecification(Specification):
    specs: Tuple[Specification, ...]

    def is_satisfied(
        self,
        item: Any,
    ) -> bool:
        return all(spec.is_satisfied(item) for spec in self.specs)


@dataclass(frozen=True)
class IsStringSpec(Specification):
    def is_satisfied(
        self,
        item: Any,
    ) -> bool:
        return isinstance(item, str)


@dataclass(frozen=True)
class IsNumericSpec(Specification):
    def is_satisfied(
        self,
        item: str,
    ) -> bool:
        cleaned_item = item.replace(" ", "").replace("-", "").replace("+", "")

        if not cleaned_item.isdigit():
            raise PhoneNumberContainsNotOnlyDigitsException()
        return True
