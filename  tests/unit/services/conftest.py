import pytest

from core.apps.orders.services.validate_products import (
    BaseValidateProductService,
    ORMValidateProductService,
)


@pytest.fixture
def product_service() -> BaseValidateProductService:
    return ORMValidateProductService()
