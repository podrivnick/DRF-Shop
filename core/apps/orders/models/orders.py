from django.contrib.auth.models import User
from django.db import models

from core.apps.common.models import TimeBaseModel
from core.apps.orders.schemas.order import OrderSchema
from core.apps.products.models.products import Product


class OrderitemQueryset(models.QuerySet):

    def total_price(self):
        return sum(cart.products_price() for cart in self)

    def total_quantity(self):
        if self:
            return sum(cart.quantity for cart in self)
        return 0


class Order(TimeBaseModel):
    user = models.ForeignKey(
        to=User, on_delete=models.SET_DEFAULT,
        null=False, verbose_name='Пользователь', blank=False, default=1,
    )
    name_receiver = models.CharField(max_length=50, verbose_name='Имя получателя', null=False)
    phone_number = models.CharField(max_length=22, verbose_name='Номер телефона')
    required_delivery = models.BooleanField(default=True, verbose_name='Требуется доставка')
    delivery_address = models.CharField(max_length=100, verbose_name='Место доставки')
    payment_on_get = models.BooleanField(default=True, verbose_name='Оплата при получении')
    has_paid = models.BooleanField(default=False, verbose_name='Оплачено')
    status = models.TextField(max_length=40, default='Обрабатывается', verbose_name='Статус заказа')
    email = models.EmailField(max_length=80, blank=False, verbose_name='Почта', null=False)
    total_price = models.DecimalField(max_digits=17, decimal_places=3, default=0, null=False, verbose_name='Общая стоимость')

    class Meta:
        db_table = "order"
        verbose_name = "Заказ"
        verbose_name_plural = "Заказы"

    def __str__(self):
        return f"Заказ № {self.pk} | Покупатель {self.user.first_name} {self.user.last_name}"

    @classmethod
    def from_entity(
        cls,
        order: OrderSchema,
    ) -> 'Order':
        return cls(
            user=order.user,
            name_receiver=order.name_receiver,
            phone_number=order.phone_number,
            required_delivery=order.required_delivery,
            delivery_address=order.delivery_address,
            payment_on_get=order.payment_on_get,
            email=order.email,
            total_price=order.total_price,
        )


class OrdersItem(models.Model):
    order = models.ForeignKey(to=Order, on_delete=models.CASCADE, verbose_name="Заказ")
    product = models.ForeignKey(
        to=Product, on_delete=models.SET_DEFAULT,
        null=False, verbose_name="Продукт", default=1,
    )
    title = models.CharField(max_length=150, verbose_name="Название")
    price = models.DecimalField(max_digits=7, decimal_places=2, verbose_name="Цена")
    quantity = models.PositiveIntegerField(default=0, verbose_name="Количество")

    class Meta:
        db_table = "orders_item"
        verbose_name = "Заказанный товар"
        verbose_name_plural = "Заказанные товары"

    objects = OrderitemQueryset.as_manager()

    def products_price(self):
        return round(self.product.sell_price() * self.quantity, 2)

    def __str__(self):
        return f"Товар {self.name} | Заказ № {self.order.pk}"
