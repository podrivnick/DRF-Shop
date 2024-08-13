from dataclasses import dataclass


@dataclass()
class BaseExceptionValidation(Exception):
    @property
    def message(self):
        return 'Something went wrong'
