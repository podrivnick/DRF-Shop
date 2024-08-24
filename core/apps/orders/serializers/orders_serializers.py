from rest_framework import serializers


def validate_quantity(value):
    if value < 1:
        raise serializers.ValidationError("Quantity must be at least 1.")
    return value


class OrderItemSerializer(serializers.Serializer):
    product_id = serializers.IntegerField()
    quantity = serializers.IntegerField(default=1, validators=[validate_quantity])


class OrdersSerializer(serializers.Serializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    name_receiver = serializers.CharField(max_length=60)
    phone_number = serializers.CharField(max_length=60)
    order_items = OrderItemSerializer(many=True)
    required_delivery = serializers.BooleanField(default=False)
    delivery_address = serializers.CharField(max_length=60)
    payment_on_get = serializers.BooleanField(default=True)
    email = serializers.EmailField()

    def to_entity(self):
        return {
            'user': self.validated_data.get('user'),
            'name_receiver': self.validated_data.get('name_receiver'),
            'phone_number': self.validated_data.get('phone_number'),
            'order_items': self.validated_data.get('order_items'),
            'required_delivery': self.validated_data.get('required_delivery'),
            'delivery_address': self.validated_data.get('delivery_address'),
            'payment_on_get': self.validated_data.get('payment_on_get'),
            'email': self.validated_data.get('email'),
            'total_price': None,
        }
