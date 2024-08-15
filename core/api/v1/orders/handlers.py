from rest_framework import (
    generics,
    permissions,
    status,
)
from rest_framework.response import Response

from core.apps.orders.serializers.orders_serializers import OrdersSerializer
from core.apps.orders.use_cases.orders import CreateOrdersUseCase


class CreateOrdersAPI(generics.CreateAPIView):
    serializer_class = OrdersSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        validated_data = serializer.initial_data

        service = CreateOrdersUseCase()
        service.execute(validated_data['order_items'])

        return Response(serializer.initial_data, status=status.HTTP_201_CREATED, headers=self.headers)
