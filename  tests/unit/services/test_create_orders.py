from decimal import Decimal
from unittest.mock import (
    call,
    MagicMock,
    patch,
)

from django.contrib.auth.models import User
from django.db import DatabaseError

import pytest

from core.apps.orders.schemas.order import (
    OrderItemsSchema,
    OrderSchema,
)
from core.apps.orders.services.order_service import (
    BaseOrderCreateService,
    OrderItemsCreationException,
    ORMCreateOrderService,
)


class TestORMCreateOrderService:

    @pytest.mark.django_db
    @patch('core.apps.orders.services.order_service.OrderModel')
    def test_create_order_success(self, MockOrderModel, user):
        """Тест успешного создания заказа.

        Этот тест проверяет, что метод `create_order` класса `ORMCreateOrderService`
        корректно создает заказ, вызывая метод `from_entity` модели `OrderModel`
        и сохраняет его в базе данных.

        Шаги:
        1. **Arrange**:
            - Создается экземпляр `ORMCreateOrderService`.
            - Определяются тестовые данные для заказа в виде словаря и преобразуются в `OrderSchema`.
            - Настраиваются моки: `MockOrderModel.from_entity` возвращает мок объекта заказа (`mock_order_dto`), а метод `save` мока также настраивается.

        2. **Act**:
            - Вызывается метод `create_order` с тестовыми данными.

        3. **Assert**:
            - Проверяется, что `from_entity` был вызван один раз с ожидаемыми аргументами.
            - Проверяется, что метод `save` на мок-объекте был вызван один раз.
            - Проверяется, что результат работы метода равен ожидаемому значению (ID заказа).

        Ожидаемый результат:
        - Метод `from_entity` должен быть вызван один раз с переданным `order_schema`.
        - Метод `save` должен быть вызван один раз.
        - Возвращаемое значение метода `create_order` должно быть равно 1.

        """  # noqa

        # Arrange
        service: BaseOrderCreateService = ORMCreateOrderService()
        user = User.objects.get(pk=1)
        data_order = {
            'user': user,   # testuser noqa
            'name_receiver': 'John Doe',
            'phone_number': '+3454345453235556',
            'order_items': [
                {'product_id': 1, 'quantity': 1},
                {'product_id': 2, 'quantity': 1},
            ],
            'required_delivery': False,
            'delivery_address': 'Zubenhp',
            'payment_on_get': False,
            'email': 'vp41919@gmail.com',
            'total_price': 100.00,
        }
        order_schema = OrderSchema(**data_order)

        mock_order_dto = MagicMock()
        mock_order_dto.pk = 1
        MockOrderModel.from_entity.return_value = mock_order_dto
        mock_order_dto.save = MagicMock(return_value=None)

        result = service.create_order(order=order_schema)
        print("MockOrderModel.from_entity.call_args_list:", MockOrderModel.from_entity.call_args_list)
        print("MockOrderModel.from_entity.call_count:", MockOrderModel.from_entity.call_count)

        # Main Tests
        MockOrderModel.from_entity.assert_called_once_with(order=order_schema)
        mock_order_dto.save.assert_called_once()

        assert result == 1

    @pytest.mark.django_db
    @patch('core.apps.orders.services.order_service.OrdersItemModel')
    @patch('core.apps.orders.services.order_service.transaction.atomic')
    def test_create_order_items_success(self, MockTransactionAtomic, MockOrdersItem):
        """Тест успешного создания товаров заказа.

        Этот тест проверяет, что метод `create_order_items` класса `ORMCreateOrderService`
        корректно создает элементы заказа, используя метод `from_entity` модели `OrdersItemModel`
        и выполняет операцию `bulk_create`.

        Шаги:
        1. **Arrange**:
            - Создается экземпляр `ORMCreateOrderService`.
            - Определяются тестовые данные для элементов заказа и преобразуются в `OrderItemsSchema`.
            - Настраиваются моки: `MockOrdersItem.from_entity` возвращает моки объектов элементов заказа, а `bulk_create` настроен для проверки вызова.

        2. **Act**:
            - Вызывается метод `create_order_items` с тестовыми данными.

        3. **Assert**:
            - Проверяется, что метод `from_entity` был вызван с правильными аргументами для каждого элемента заказа.
            - Проверяется, что метод `bulk_create` был вызван один раз с правильными аргументами.
            - Проверяется, что результат работы метода соответствует ожидаемому значению.

        Ожидаемый результат:
        - Метод `from_entity` должен быть вызван для каждого элемента заказа.
        - Метод `bulk_create` должен быть вызван один раз с правильным списком элементов заказа.
        - Результат работы метода `create_order_items` должен соответствовать ожидаемому значению в формате `OrderItemsSchema`.

        """  # noqa

        # Arrange
        service: BaseOrderCreateService = ORMCreateOrderService()

        order_items_schema = OrderItemsSchema(
            items=[
                {'product': 1, 'title': 'charge', 'discount': 50, 'price': 500, 'quantity': 1},
                {'product': 3, 'title': 'monitor', 'discount': 0, 'price': 1000, 'quantity': 1},
            ],
        )

        # Create mock objects for each item
        mock_order_items = [MagicMock() for _ in order_items_schema.items]

        # Set the return value for from_entity method
        MockOrdersItem.from_entity.side_effect = mock_order_items
        MockOrdersItem.objects.bulk_create = MagicMock()

        # Act
        result = service.create_order_items(order_id=1, order_items=order_items_schema)

        # Assert
        expected_calls = [
            call(order_id=1, item_product=item) for item in order_items_schema.items
        ]

        MockOrdersItem.from_entity.assert_has_calls(expected_calls)
        MockOrdersItem.objects.bulk_create.assert_called_once_with(mock_order_items)

        # Convert order_items_schema to expected result format if necessary
        expected_result = OrderItemsSchema(
            items=[
                {'product': 1, 'title': 'charge', 'price': Decimal('500'), 'quantity': 1, 'discount': Decimal('50')},
                {'product': 3, 'title': 'monitor', 'price': Decimal('1000'), 'quantity': 1, 'discount': Decimal('0')},
            ],
        )

        assert result == expected_result

    @pytest.mark.django_db
    @patch('core.apps.orders.services.order_service.OrdersItemModel')
    @patch('core.apps.orders.services.order_service.transaction.atomic')
    def test_create_order_items_database_error(self, MockTransactionAtomic, MockOrdersItem):
        """Тест обработки ошибки базы данных при создании элементов заказа.

        Этот тест проверяет, что метод `create_order_items` класса `ORMCreateOrderService`
        корректно обрабатывает ошибку базы данных, выбрасывая исключение `OrderItemsCreationException`
        при возникновении `DatabaseError`.

        Шаги:
        1. **Arrange**:
            - Создается экземпляр `ORMCreateOrderService`.
            - Определяются тестовые данные для элементов заказа и преобразуются в `OrderItemsSchema`.
            - Настраивается мок для метода `bulk_create`, чтобы он выбрасывал `DatabaseError`.

        2. **Act / Assert**:
            - Вызов метода `create_order_items` внутри блока `pytest.raises` проверяет, что метод правильно выбрасывает исключение `OrderItemsCreationException`.

        Ожидаемый результат:
            - Метод `create_order_items` должен выбросить `OrderItemsCreationException`, если метод `bulk_create` вызывает `DatabaseError`.

        """  # noqa

        # Arrange
        service: BaseOrderCreateService = ORMCreateOrderService()
        order_items_schema = OrderItemsSchema(
            items=[
                {'product': 1, 'title': 'charge', 'discount': 50, 'price': 500, 'quantity': 1},
            ],
        )
        MockOrdersItem.objects.bulk_create.side_effect = DatabaseError("Database error")

        # Act / Assert
        with pytest.raises(OrderItemsCreationException):
            service.create_order_items(order_id=1, order_items=order_items_schema)
