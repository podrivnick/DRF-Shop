from rest_framework import viewsets

from django_filters.rest_framework import DjangoFilterBackend

from core.apps.products.models.products import Product as ProductModel
from core.apps.products.serializers.products import ProductSerializer
from core.apps.products.services.products import ProductsFilterByDiscountAndQuantity


class ProductAPIList(
    viewsets.ReadOnlyModelViewSet,
):
    queryset = ProductModel.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = ProductsFilterByDiscountAndQuantity
