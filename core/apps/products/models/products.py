from django.contrib.postgres.fields import ArrayField
from django.db import models

from core.apps.common.models import TimeBaseModel


class Product(TimeBaseModel):
    title = models.CharField(
        max_length=128,
        verbose_name='Product Title',
    )
    description = models.TextField(
        verbose_name='Product Description',
    )
    discount = models.DecimalField(
        blank=True,
        max_digits=10,
        decimal_places=2,
        default=0.00,
        verbose_name='Product Discount',
    )
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name='Product Price',
    )
    quantity = models.PositiveIntegerField(
        default=1,
        verbose_name='Product Quantity',
    )
    tags = ArrayField(
        base_field=models.CharField(max_length=100),
        default=list,
        verbose_name='Products Tags',
    )

    def sell_price(self) -> int:
        if self.discount:
            return round(self.price - self.price * self.discount / 100, 2)

        return self.price

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"
