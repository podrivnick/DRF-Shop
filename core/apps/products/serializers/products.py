from rest_framework import serializers

from core.apps.products.models.products import Product as ProductModel


class ProductSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = ProductModel
        fields = "__all__"
