r"""
1. Test products filtration: Is products data valid   noqa
2. Test products filtration: Non-exist product ID   noqa
3. Test products filtration: Too much quantity   noqa
"""

import pytest

from core.apps.orders.exceptions.database_orders_exceptions import (
    NotEnoughQuantityProducts,
    NotFoundProductException,
)
from core.apps.orders.schemas.order import (
    OrderItemsSchema,
    ValidateProductsQuantityId,
)
from core.apps.orders.services.validate_products import ORMValidateProductService

from ..factories.products import ProductModelFactory


@pytest.mark.django_db
def test_check_products_valid():
    # Tests Products
    product_1 = ProductModelFactory.create(pk=1, quantity=10, price=1000, discount=50, title="charge")   # noqa
    product_2 = ProductModelFactory.create(pk=3, quantity=5, price=1000, discount=0, title="monitor")   # noqa

    # Expected data for response
    all_data_products = OrderItemsSchema(
        items=[
            {'product': 1, 'title': 'charge', 'discount': 50, 'price': 500, 'quantity': 1},
            {'product': 3, 'title': 'monitor', 'discount': 0, 'price': 1000, 'quantity': 1},
        ],
    )

    # Enter data for testing
    order_items_data = ValidateProductsQuantityId(
        list_of_product_quntity_and_ids=[
            {'product_id': 1, 'quantity': 1},
            {'product_id': 3, 'quantity': 1},
        ],
    )

    service = ORMValidateProductService()

    total_price, response_all_data_products = service.check_products(order_items_data=order_items_data)

    assert total_price == 1500, f"total_price: {total_price}"
    assert response_all_data_products == all_data_products, f"getting schema --- {response_all_data_products}"


@pytest.mark.django_db
def test_check_products_not_found():
    product_1 = ProductModelFactory.create(pk=1, quantity=10, price=100)  # noqa

    order_items_data = ValidateProductsQuantityId(
        list_of_product_quntity_and_ids=[
            {'product_id': 1, 'quantity': 2},
            {'product_id': 2, 'quantity': 1},
        ],
    )

    service = ORMValidateProductService()

    with pytest.raises(NotFoundProductException) as exc_info:
        service.check_products(order_items_data=order_items_data)

    assert exc_info.value.product == 2  # Check that the exception is related to the product with ID 2


@pytest.mark.django_db
def test_check_products_not_enough_quantity():
    # Tests Products
    product_1 = ProductModelFactory.create(pk=1, quantity=1, price=100)  # noqa

    order_items_data = ValidateProductsQuantityId(
        list_of_product_quntity_and_ids=[
            {'product_id': 1, 'quantity': 2},
        ],
    )

    service = ORMValidateProductService()

    with pytest.raises(NotEnoughQuantityProducts) as exc_info:
        service.check_products(order_items_data=order_items_data)

    assert exc_info.value.product == 1  # Check that the exception is related to the product with ID 1
