from dataclasses import dataclass

from core.apps.orders.exceptions.orders_exceptions import BaseExceptionOrder
from core.apps.orders.schemas.order import (
    OrderSchema,
    ValidateProductsQuantityId,
)
from core.apps.orders.services.order_service import BaseOrderCreateService
from core.apps.orders.services.validate_products import BaseValidateProductService
from core.apps.orders.services.validation_order import BaseValidationOrderService


@dataclass
class CreateOrdersUseCase:
    validator_order: BaseValidationOrderService
    validate_products: BaseValidateProductService
    order: BaseOrderCreateService

    def execute(
        self,
        serializer: dict,
    ) -> OrderSchema:
        try:
            validate_order_checker = self.validator_order.validated_data_order(
                serializer['name_receiver'],
                serializer['phone_number'],
                serializer['delivery_address'],
                serializer['email'],
            )
            print(validate_order_checker)
        except ValueError:
            raise ValueError("Invalid name receiver kookkokok")

        try:
            order_products_data = ValidateProductsQuantityId(
                list_of_product_quntity_and_ids=serializer["order_items"],
            )

            total_price, products_required_data = self.validate_products.check_products(
                order_items_data=order_products_data,
            )

        except BaseExceptionOrder as error:
            print(error.message)

        serializer['total_price'] = total_price
        print(serializer)
        order_dto = self.order.create_order(OrderSchema(**serializer))

        try:
            self.order.create_order_items(order_dto, products_required_data)
        except BaseExceptionOrder as exception:
            print(exception.message)

        return order_dto
