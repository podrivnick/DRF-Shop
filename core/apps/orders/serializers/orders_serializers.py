from rest_framework import serializers

from core.apps.orders.models.orders import Order


class OrderItemSerializer(serializers.Serializer):
    product_id = serializers.IntegerField()
    quantity = serializers.IntegerField(default=1)


class OrdersSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    name_receiver = serializers.CharField(max_length=60)
    phone_number = serializers.CharField(max_length=60)
    order_items = OrderItemSerializer(many=True)
    required_delivery = serializers.BooleanField(default=False)
    delivery_address = serializers.CharField(max_length=100)
    payment_on_get = serializers.BooleanField(default=True)
    total_price = serializers.IntegerField()

    class Meta:
        model = Order
        fields = [
            'user',
            'name_receiver',
            'phone_number',
            'order_items',
            'required_delivery',
            'delivery_address',
            'payment_on_get',
            'total_price',
        ]
