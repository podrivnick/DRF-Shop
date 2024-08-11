from django.urls import (
    include,
    path,
)
from rest_framework import routers

from core.api.v1.products.handlers import ProductAPIList


router = routers.SimpleRouter()
router.register(r'products', ProductAPIList, basename='products')

urlpatterns = [
    path('', include(router.urls)),
]
