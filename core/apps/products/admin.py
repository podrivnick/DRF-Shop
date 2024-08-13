from django.contrib import admin

from core.apps.products.models.products import Product as ProductModel


@admin.register(ProductModel)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'title',
        'description',
        'discoint',
        'price',
        'quantity',
        'tags',
        'created_at',
        'updated_at',
    )
