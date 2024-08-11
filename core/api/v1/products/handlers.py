from rest_framework import viewsets

from core.apps.products.models.products import Product as ProductModel
from core.apps.products.serializers.products import ProductSerializer


class ProductAPIList(
    viewsets.ReadOnlyModelViewSet,
):
    queryset = ProductModel.objects.all()
    serializer_class = ProductSerializer
