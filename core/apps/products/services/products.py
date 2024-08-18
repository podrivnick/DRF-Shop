from abc import (
    ABC,
    abstractmethod,
)
from typing import Iterable

from core.apps.products.models.products import Product as ProductModel


class BaseProductsFilter(ABC):
    @abstractmethod
    def filter_products(self):
        raise NotImplementedError


class ProductsFilterById(BaseProductsFilter):
    def filter_products(self, product_ids: Iterable):
        return ProductModel.objects.filter(pk__in=product_ids)
