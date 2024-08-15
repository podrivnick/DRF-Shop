from rest_framework import serializers


class OrderItemSerializer(serializers.Serializer):
    product_id = serializers.IntegerField()
    quantity = serializers.IntegerField(default=1)


class OrdersSerializer(serializers.Serializer):
    name_receiver = serializers.CharField(max_length=60)
    phone_number = serializers.CharField(max_length=60)
    order_items = OrderItemSerializer(many=True)
    required_delivery = serializers.BooleanField(default=False)
    delivery_address = serializers.CharField(max_length=100)
    payment_on_get = serializers.BooleanField(default=True)
    email = serializers.EmailField()

    def validate_email(self, value):
        if len(value) <= 0:
            raise serializers.ValidationError('Email must be a more than zero length')
        return value
