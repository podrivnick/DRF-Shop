from dataclasses import dataclass

from core.apps.orders.config.order_config import (
    MAX_LENGTH_DELIVERY_ADDRESS,
    MAX_LENGTH_NAME_RECEIVER,
    MAX_LENGTH_PHONE_NUMBER,
)
from core.apps.orders.schemas.base_validator import BaseValidatorOrder
from core.apps.orders.utils.base_spec import (
    IsNumericSpec,
    IsStringSpec,
)
from core.apps.orders.utils.validators_order import (
    AllowedCharactersSpec,
    IsAlphabeticSpec,
    IsNotEmptySpec,
    MaxLengthSpec,
    NoSpecialCharactersSpec,
    ValidDomainSpec,
    ValidEmailSpec,
)


@dataclass(frozen=True)
class NameReceiver(BaseValidatorOrder[str]):
    def validate(self):
        pass

        name_receiver_spec = IsStringSpec().and_spec(IsNotEmptySpec()).\
                                and_spec(MaxLengthSpec(MAX_LENGTH_NAME_RECEIVER)).\
                                and_spec(IsAlphabeticSpec())   # noqa

        name_receiver_spec.is_satisfied(self.value)

    def as_generic_type(self):
        return str(self.value)


@dataclass(frozen=True)
class PhoneNumber(BaseValidatorOrder[str]):
    def validate(self):
        phone_number_spec = IsNumericSpec().and_spec(IsNotEmptySpec()).\
                                and_spec(MaxLengthSpec(MAX_LENGTH_PHONE_NUMBER)).\
                                and_spec(AllowedCharactersSpec())  # noqa

        phone_number_spec.is_satisfied(self.value)

    def as_generic_type(self):
        return str(self.value)


@dataclass(frozen=True)
class DeliveryAddress(BaseValidatorOrder[str]):
    def validate(self):
        delivery_address_spec = IsStringSpec().and_spec(IsNotEmptySpec()).\
                                    and_spec(MaxLengthSpec(MAX_LENGTH_DELIVERY_ADDRESS)).\
                                    and_spec(NoSpecialCharactersSpec())  # noqa

        delivery_address_spec.is_satisfied(self.value)

    def as_generic_type(self):
        return str(self.value)


@dataclass(frozen=True)
class Email(BaseValidatorOrder[str]):
    def validate(self):
        email_spec = IsStringSpec().and_spec(IsNotEmptySpec()).\
                        and_spec(ValidDomainSpec()).\
                        and_spec(ValidEmailSpec())   # noqa

        email_spec.is_satisfied(self.value)

    def as_generic_type(self):
        return str(self.value)
