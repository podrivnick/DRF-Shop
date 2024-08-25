import pytest

from core.apps.orders.services.validate_products import (
    BaseValidateProductService,
    ORMValidateProductService,
)


# Test Product Services
@pytest.fixture
def product_service() -> BaseValidateProductService:
    return ORMValidateProductService()
