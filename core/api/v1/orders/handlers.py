from rest_framework import (
    generics,
    permissions,
    status,
)
from rest_framework.response import Response

from core.apps.orders.serializers.orders_serializers import OrdersSerializer


class CreateOrdersAPI(generics.CreateAPIView):
    serializer_class = OrdersSerializer
    permission_classes = [permissions.IsAuthenticated]

    def create(self, request, *args, **kwargs) -> Response:
        serializer = self.get_serializer(data=request.data)

        return Response(serializer.initial_data, status=status.HTTP_201_CREATED, headers=self.headers)
