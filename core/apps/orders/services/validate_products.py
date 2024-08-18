from abc import (
    ABC,
    abstractmethod,
)

from core.apps.orders.exceptions.orders_exceptions import (
    NotEnoughQuantityProducts,
    NotFoundProductException,
)
from core.apps.products.models.products import Product as ProductModel


class BaseValidateProductService(ABC):
    @abstractmethod
    def check_products(self) -> list:
        raise NotImplementedError


class ORMValidateProductService(BaseValidateProductService):
    # *order_items_data: [{'product_id': 1, 'quantity': 2}, {'product_id': 3, 'quantity': 1}]
    def check_products(self, order_items_data: list) -> int:
        # All ID's are required
        product_ids = (item['product_id'] for item in order_items_data)

        products = ProductModel.objects.filter(pk__in=product_ids)

        products_dict = {product.pk: product for product in products}

        total_price = 0
        all_data_products = []

        for product in order_items_data:
            product_id = product['product_id']
            quantity = product['quantity']

            if product_id not in products_dict:
                raise NotFoundProductException(product=product_id)

            if products_dict[product_id].quantity >= quantity:
                price_with_quantity = products_dict[product_id].sell_price() * quantity

                total_price += price_with_quantity

                all_data_products.append(
                    {
                        'product': product_id,
                        'title': products_dict[product_id].title,
                        'price': price_with_quantity,
                        'quantity': quantity,
                    },
                )
            else:
                raise NotEnoughQuantityProducts(product=product_id)

        return total_price, all_data_products
