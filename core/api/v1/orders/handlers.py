from logging import Logger

from rest_framework import (
    generics,
    permissions,
    status,
)

import orjson

from core.api.base_response import StandartResponseAPI
from core.apps.common.base_exceptions import (
    CustomExceptionForUseCaseOrder,
    ServiceException,
)
from core.apps.orders.serializers.orders_serializers import OrdersSerializer
from core.apps.orders.use_cases.orders import CreateOrdersUseCase
from core.project.containers import get_container


class CreateOrdersAPI(
    generics.CreateAPIView,
    StandartResponseAPI,
):
    serializer_class = OrdersSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        container = get_container()
        use_case: CreateOrdersUseCase = container.resolve(CreateOrdersUseCase)

        try:
            result = use_case.execute(
                serializer=serializer.to_entity(),
            )

            return self.create_response(
                data=result,
                status_code=status.HTTP_201_CREATED,
                message="Order created successfully",
            )
        except ServiceException as error:
            logger: Logger = container.resolve(Logger)
            logger.error(msg='User could not create review', extra={'error_meta': orjson.dumps(error).decode()})

            raise CustomExceptionForUseCaseOrder(
                detail=error.message,
                status_code=422,
                extra_data={'some_field': 'some_value'},
            )
