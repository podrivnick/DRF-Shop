from dataclasses import dataclass

from rest_framework.exceptions import APIException

from core.apps.common.config import (
    BASE_EXCEPTION_VALIDATION,
    SERVICE_EXCEPTION_VALIDATION,
    USE_CASE_EXCEPTION_ORDER,
)


@dataclass()
class BaseExceptionValidation(Exception):
    @property
    def message(self):
        return BASE_EXCEPTION_VALIDATION


@dataclass(eq=False)
class ServiceException(Exception):
    @property
    def message(self):
        return SERVICE_EXCEPTION_VALIDATION


class CustomExceptionForUseCaseOrder(APIException):
    status_code = 422
    default_detail = USE_CASE_EXCEPTION_ORDER
    default_code = 'invalid'

    def __init__(self, detail=None, status_code=None, extra_data=None):
        if status_code is not None:
            self.status_code = status_code
        if detail is not None:
            self.detail = detail
        if extra_data is not None:
            self.extra_data = extra_data

    def __str__(self):
        return str(self.detail)
