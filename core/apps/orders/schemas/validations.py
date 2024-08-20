from dataclasses import dataclass

from core.apps.orders.schemas.base_validator import BaseValidatorOrder


@dataclass(frozen=True)
class NameReceiver(BaseValidatorOrder[str]):
    def validate(self):
        if not isinstance(self.value, str) or len(self.value) > 60:
            raise ValueError("Invalid name receiver kookkokok")

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
