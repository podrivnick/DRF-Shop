from abc import (
    ABC,
    abstractmethod,
)
from typing import Iterable

from django_filters import rest_framework as filters

from core.apps.products.models.products import Product as ProductModel


class BaseProductsFilter(ABC):
    @abstractmethod
    def filter_products(self):
        raise NotImplementedError


class ProductsFilterById(BaseProductsFilter):
    def filter_products(self, product_ids: Iterable):
        return ProductModel.objects.filter(pk__in=product_ids)


class ProductsFilterByDiscountAndQuantity(filters.FilterSet):
    in_stock = filters.BooleanFilter(method='filter_in_stock')
    discount = filters.NumberFilter(field_name="discount", lookup_expr='gt')

    class Meta:
        model = ProductModel
        fields = ['in_stock', 'discount']

    def filter_in_stock(self, queryset, name, value):
        if value is True:
            return queryset.filter(quantity__gt=0)
        else:
            return queryset.filter(quantity=0)
