import pytest

from core.apps.orders.services.validate_products import (
    BaseValidatePriductService,
    ORMValidateProductService,
)


@pytest.fixture
def product_service() -> BaseValidatePriductService:
    return ORMValidateProductService()
