from django.contrib import admin

from core.apps.orders.models.orders import (
    Order,
    OrdersItem,
)


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'user',
        'name_receiver',
        'phone_number',
        'delivery_address',
        'payment_on_get',
        'has_paid',
        'status',
        'email',
        'total_price',
        'created_at',
        'updated_at',
    )


@admin.register(OrdersItem)
class OrdersItemAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'order',
        'product',
        'title',
        'price',
        'quantity',
    )
