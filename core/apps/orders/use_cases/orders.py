from dataclasses import dataclass

from core.apps.orders.services.validate_products import ORMValidateProductService


@dataclass
class CreateOrdersUseCase:
    def execute(
        self,
        serializer,
    ) -> int:
        validate_products = ORMValidateProductService()
        total_price = validate_products.check_products(serializer)

        print(f"Total price ------ {total_price}")
        return total_price if total_price else ValueError('Kal')
