from abc import (
    ABC,
    abstractmethod,
)
from dataclasses import dataclass

from core.apps.orders.schemas.validations import (
    DeliveryAddress,
    Email,
    NameReceiver,
    PhoneNumber,
)


@dataclass(eq=False)
class BaseValidationOrderService(ABC):
    @abstractmethod
    def validated_data_order(self):
        raise NotImplementedError()


@dataclass(eq=False)
class ValidationOrderDataService(BaseValidationOrderService):
    def validated_data_order(
        self,
        name_receiver: str,
        phone_number: str,
        delivery_address: str,
        email: str,
    ) -> dict:
        name_receiver_validator = NameReceiver(name_receiver)
        phone_number_validator = PhoneNumber(phone_number)
        delivery_address_validator = DeliveryAddress(delivery_address)
        email_validator = Email(email)

        result = {
            "name_receiver": name_receiver_validator,
            "phone_number": phone_number_validator,
            "delivery_address": delivery_address_validator,
            "email": email_validator,
        }

        return result
