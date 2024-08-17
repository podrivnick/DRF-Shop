from dataclasses import dataclass

from core.apps.orders.exceptions.orders_exceptions import BaseExceptionOrder
from core.apps.orders.services.validate_products import ORMValidateProductService


# TODO: Check infructures of exceptions
@dataclass
class CreateOrdersUseCase:
    def execute(
        self,
        serializer,
    ) -> int:

        try:
            validate_products = ORMValidateProductService()
            total_price = validate_products.check_products(serializer)
        except BaseExceptionOrder as error:
            print(error.message)

        print(f"Total price ------ {total_price}")

        return total_price if total_price else ValueError('Kal')
