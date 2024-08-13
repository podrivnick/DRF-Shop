from dataclasses import dataclass

from core.apps.common.base_exceptions import BaseExceptionValidation


@dataclass
class ValidationRegisterDataExceptions(BaseExceptionValidation):
    MESSAGE: str = 'Invalid data for registration'

    @property
    def message(self):
        return self.MESSAGE
