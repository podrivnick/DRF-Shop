from core.apps.common.base_exceptions import BaseExceptionValidation
from core.apps.common.utils.repository import BaseValidator


class UserRegistrationService:
    def __init__(self, user_repository: BaseValidator, serializer):
        self.user_repository: BaseValidator = user_repository(serializer)

    def validate(self) -> bool:
        try:
            self.user_repository.is_valid_data()
            return True
        except BaseExceptionValidation as exception:
            print(exception.message)
