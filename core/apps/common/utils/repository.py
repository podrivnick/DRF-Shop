from abc import (
    ABC,
    abstractmethod,
)

from core.apps.users.exception import ValidationRegisterDataExceptions


class BaseValidator(ABC):
    @abstractmethod
    def is_valid_data(self):
        raise NotImplementedError


class ValidationRegisterData(BaseValidator):
    def __init__(self, serializer):
        self.object = serializer

    def is_valid_data(self):
        is_valid = self.object.is_valid(raise_exception=False)
        if not is_valid:
            raise ValidationRegisterDataExceptions
