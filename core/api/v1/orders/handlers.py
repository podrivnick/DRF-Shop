from logging import Logger

from rest_framework import (
    generics,
    permissions,
    status,
)
from rest_framework.response import Response

import orjson

from core.apps.common.base_exceptions import (
    CustomExceptionForUseCaseOrder,
    ServiceException,
)
from core.apps.orders.serializers.orders_serializers import OrdersSerializer
from core.apps.orders.use_cases.orders import CreateOrdersUseCase
from core.project.containers import get_container


class CreateOrdersAPI(generics.CreateAPIView):
    serializer_class = OrdersSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        container = get_container()
        use_case: CreateOrdersUseCase = container.resolve(CreateOrdersUseCase)

        try:
            result = use_case.execute(
                serializer=serializer.to_entity(),
            )

        except ServiceException as error:
            logger: Logger = container.resolve(Logger)
            logger.error(msg='User could not create review', extra={'error_meta': orjson.dumps(error).decode()})

            raise CustomExceptionForUseCaseOrder(
                detail=error.message,
                status_code=422,  # Замените на нужный статус код
                extra_data={'some_field': 'some_value'},
            )

        return Response(result, status=status.HTTP_201_CREATED, headers=self.headers)
