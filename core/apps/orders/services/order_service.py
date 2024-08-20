from abc import (
    ABC,
    abstractmethod,
)

from django.db import (
    DatabaseError,
    transaction,
)

from core.apps.orders.exceptions.database_orders_exceptions import OrderItemsCreationException
from core.apps.orders.models.orders import (
    Order as OrderModel,
    OrdersItem as OrdersItemModel,
)
from core.apps.orders.schemas.order import (
    OrderItemsSchema,
    OrderSchema,
)


class BaseOrderCreateService(ABC):
    @abstractmethod
    def create_order(
        self,
        data_order: OrderSchema,
    ) -> OrderSchema:
        raise NotImplementedError

    @abstractmethod
    def create_order_items(
        self,
        data_order_item: OrderItemsSchema,
    ) -> OrderItemsSchema:
        raise NotImplementedError


class ORMCreateOrderService(BaseOrderCreateService):
    def create_order(
        self,
        order: OrderSchema,
    ) -> OrderSchema:
        order_dto: OrderModel = OrderModel.from_entity(
            order=order,
        )
        order_dto.save()

        return order_dto.pk

    def create_order_items(
        self,
        order_id: int,
        order_items: OrderItemsSchema,
    ) -> OrderItemsSchema:
        query = [
            OrdersItemModel.from_entity(
                order_id=int(order_id),
                item_product=product,
            )
            for product in order_items.items
        ]

        try:
            with transaction.atomic():
                OrdersItemModel.objects.bulk_create(query)
        except DatabaseError as exception:
            raise OrderItemsCreationException from exception

        return order_items
