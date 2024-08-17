from dataclasses import dataclass

from core.apps.orders.exceptions.orders_exceptions import BaseExceptionOrder
from core.apps.orders.schemas.order import OrderSchema
from core.apps.orders.services.order_service import ORMCreateOrderService
from core.apps.orders.services.validate_products import ORMValidateProductService


# TODO: Check infructures of exceptions
@dataclass
class CreateOrdersUseCase:
    def execute(
        self,
        serializer,
    ) -> OrderSchema:

        try:
            validate_products = ORMValidateProductService()
            total_price = validate_products.check_products(serializer['order_items'])
        except BaseExceptionOrder as error:
            print(error.message)

        serializer['total_price'] = total_price

        order = ORMCreateOrderService()
        to_entity = order.create_order(OrderSchema(**serializer))

        print(to_entity)
        return to_entity if to_entity else ValueError('Invalid make order')
