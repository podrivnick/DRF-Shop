from abc import (
    ABC,
    abstractmethod,
)
from dataclasses import dataclass
from typing import (
    Any,
    Generic,
    TypeVar,
)


VT = TypeVar('VT', bound=Any)


@dataclass(frozen=True)
class BaseValidatorOrder(ABC, Generic[VT]):
    value: VT

    def __post_init__(self):
        self.validate()

    @abstractmethod
    def validate(self):
        raise NotImplementedError()

    @abstractmethod
    def as_generic_type(self) -> VT:
        return NotImplementedError()
