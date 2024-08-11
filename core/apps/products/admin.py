from django.contrib import admin

from core.apps.products.models.products import Product as ProductModel


# Register your models here.


admin.site.register(ProductModel)
