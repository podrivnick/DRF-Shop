from django.contrib.auth.models import User
from django.test import Client

import pytest

from core.apps.orders.services.validate_products import (
    BaseValidateProductService,
    ORMValidateProductService,
)


# Test Product Services
@pytest.fixture
def product_service() -> BaseValidateProductService:
    return ORMValidateProductService()


# Test Order Services
@pytest.fixture
def user():
    return User.objects.create_user(username='testuser', password='password123')


@pytest.fixture
def client(user):
    client = Client()
    client.login(username='testuser', password='password123')
    return client
