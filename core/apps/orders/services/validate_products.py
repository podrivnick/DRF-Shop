from abc import (
    ABC,
    abstractmethod,
)

from core.apps.products.models.products import Product as ProductModel


class BaseValidatePriductService(ABC):
    @abstractmethod
    def check_products(self) -> list:
        raise NotImplementedError


class ORMValidateProductService(BaseValidatePriductService):
    # order_items_data: [{'product_id': 1, 'quantity': 2}, {'product_id': 3, 'quantity': 1}]
    def check_products(self, order_items_data: list) -> int:
        total_price = 0

        for product in order_items_data:
            try:
                is_product_exist = ProductModel.objects.get(pk=product['product_id'], quantity__gte=product['quantity'])

                total_price += is_product_exist.sell_price() * product['quantity']

            except ProductModel.DoesNotExist as exception:
                print(f'Товар с id {product['product_id']} не найден.')
                print(exception)

                continue

        return total_price
