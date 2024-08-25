from django.contrib.auth.models import User
from django.test import Client

import pytest


# Test Order Services
@pytest.fixture
def user():
    return User.objects.create_user(username='testuser', password='password123')


@pytest.fixture
def client(user):
    client = Client()
    client.login(username='testuser', password='password123')
    return client
