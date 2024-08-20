from dataclasses import dataclass

from core.apps.orders.schemas.base_validator import BaseValidatorOrder
from core.apps.orders.utils.validators_order import (
    IsAlphabeticSpec,
    IsNotEmptySpec,
    IsStringSpec,
    MaxLengthSpec,
)


@dataclass(frozen=True)
class NameReceiver(BaseValidatorOrder[str]):
    def validate(self):
        max_length_name_receiver = 60

        name_receiver_spec = IsStringSpec().and_spec(IsNotEmptySpec()).\
                                and_spec(MaxLengthSpec(max_length_name_receiver)).\
                                and_spec(IsAlphabeticSpec())   # noqa

        name_receiver_spec.is_satisfied(self.value)

    def as_generic_type(self):
        return str(self.value)


@dataclass(frozen=True)
class PhoneNumber(BaseValidatorOrder[str]):
    def validate(self):
        if not isinstance(self.value, str) or len(self.value) > 60:
            raise ValueError("Invalid name receiver")

    def as_generic_type(self):
        return str(self.value)


@dataclass(frozen=True)
class DeliveryAddress(BaseValidatorOrder[str]):
    def validate(self):
        if not isinstance(self.value, str) or len(self.value) > 60:
            raise ValueError("Invalid name receiver")

    def as_generic_type(self):
        return str(self.value)


@dataclass(frozen=True)
class Email(BaseValidatorOrder[str]):
    def validate(self):
        if not isinstance(self.value, str) or len(self.value) > 60:
            raise ValueError("Invalid name receiver")

    def as_generic_type(self):
        return str(self.value)
