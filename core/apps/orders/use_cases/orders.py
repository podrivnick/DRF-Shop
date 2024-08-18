from dataclasses import dataclass

from core.apps.orders.exceptions.orders_exceptions import BaseExceptionOrder
from core.apps.orders.schemas.order import (
    OrderItemsSchema,
    OrderSchema,
)
from core.apps.orders.services.order_service import ORMCreateOrderService
from core.apps.orders.services.validate_products import ORMValidateProductService


@dataclass
class CreateOrdersUseCase:
    def execute(
        self,
        serializer,
    ) -> OrderSchema:

        try:
            validate_products = ORMValidateProductService()
            total_price, products_required_id = validate_products.check_products(serializer['order_items'])
        except BaseExceptionOrder as error:
            print(error.message)

        serializer['total_price'] = total_price

        order = ORMCreateOrderService()

        order_dto = order.create_order(OrderSchema(**serializer))
        try:
            create_order_items = order.create_order_items(order_dto, OrderItemsSchema(products_required_id))
        except BaseExceptionOrder as exception:
            print(exception.message)

        print(f"{order_dto} to ----- {create_order_items}")

        return order_dto if order_dto else ValueError('Invalid make order')
