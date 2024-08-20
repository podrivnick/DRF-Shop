from abc import (
    ABC,
    abstractmethod,
)
from dataclasses import (
    dataclass,
    field,
)
from typing import (
    Any,
    Tuple,
)

from core.apps.orders.exceptions.validation_orders_exceptions import (
    IsNameReceiverNotAlphabeticSpec,
    NameReceiverIsEmpty,
    TooMuchLengthNameReceiver,
)


@dataclass(frozen=True)
class Specification(ABC):
    @abstractmethod
    def is_satisfied(self, item: Any) -> bool:
        pass

    def and_spec(self, other: 'Specification') -> 'AndSpecification':
        return AndSpecification((self, other))


@dataclass(frozen=True)
class AndSpecification(Specification):
    specs: Tuple[Specification, ...]

    def is_satisfied(self, item: Any) -> bool:
        return all(spec.is_satisfied(item) for spec in self.specs)


@dataclass(frozen=True)
class IsStringSpec(Specification):
    def is_satisfied(self, item: Any) -> bool:
        return isinstance(item, str)


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
