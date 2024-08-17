import factory
from factory.django import DjangoModelFactory
from faker import Faker

from core.apps.products.models.products import Product


fake = Faker()


class ProductModelFactory(DjangoModelFactory):
    title = factory.Faker('word')
    description = factory.Faker('sentence')
    discount = factory.Faker('pydecimal', left_digits=2, right_digits=2, min_value=0)
    price = factory.Faker('pydecimal', left_digits=4, right_digits=2, positive=True, min_value=1000, max_value=100000)
    quantity = factory.Faker('random_int', min=1, max=100)
    tags = factory.List([fake.word() for _ in range(3)])

    class Meta:
        model = Product
