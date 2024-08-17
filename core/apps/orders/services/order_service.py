from abc import (
    ABC,
    abstractmethod,
)

from core.apps.orders.models.orders import (  # noqa
    Order as OrderModel,
    OrdersItem as OrdersItemModel,
)
from core.apps.orders.schemas.order import OrderSchema


class BaseOrderCreateService(ABC):
    @abstractmethod
    def create_order(self, data_order: OrderSchema) -> OrderSchema:
        raise NotImplementedError


class ORMCreateOrderService(BaseOrderCreateService):
    def create_order(self, order: OrderSchema) -> OrderSchema:
        order_dto: OrderModel = OrderModel.from_entity(
            order=order,
        )
        order_dto.save()

        return order
