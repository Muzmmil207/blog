import factory
import pytest
from faker import Faker
from pytest_factoryboy import register

fake = Faker()

from apps.authors.models import Author
from apps.dashboard.models import Category


class AuthorFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Author
    
    username = fake.name()
    is_staff = 'True'

class CategoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Category

    author = factory.SubFactory(AuthorFactory)
    # name = factory.Sequence(lambda n: "cat_slug_%d" % n)
    name = fake.lexify(text="cat_name_??????")
    slug = fake.lexify(text="cat_slug_??????")


register(CategoryFactory)
