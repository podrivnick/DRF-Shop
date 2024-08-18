from functools import lru_cache
from logging import (
    getLogger,
    Logger,
)

import punq

from core.apps.orders.services.order_service import (
    BaseOrderCreateService,
    ORMCreateOrderService,
)
from core.apps.orders.services.validate_products import (
    BaseValidateProductService,
    ORMValidateProductService,
)
from core.apps.orders.use_cases.orders import CreateOrdersUseCase


@lru_cache(1)
def get_container() -> punq.Container:
    return _initialize_container()


def _initialize_container() -> punq.Container:
    container = punq.Container()

    # init internal stuff
    container.register(Logger, factory=getLogger, name='django.request')

    # init services
    container.register(BaseValidateProductService, ORMValidateProductService)
    container.register(BaseOrderCreateService, ORMCreateOrderService)  # noqa  

    # init use cases
    container.register(CreateOrdersUseCase)

    return container
