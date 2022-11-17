import datetime

import factory
import pytest
from faker import Faker
from pytest_factoryboy import register

from django.utils.timezone import now

fake = Faker()

from apps.authors.models import Author
from apps.dashboard.models import (
    Category, Post, PostComment, PostImage, PostMeta, PostTags,
)


class AuthorFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Author
    
    username = factory.Sequence(lambda n: "username_??????%d" % n)
    email = factory.LazyAttribute(lambda a: "{0}.{1}@example.com".format(a.first_name, a.last_name).lower())
    first_name = factory.Faker("first_name")
    last_name = factory.Faker("last_name")
    mobile_number = factory.Sequence(lambda n: "+249011333672%d" % n)

class CategoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Category

    author = factory.SubFactory(AuthorFactory)
    # name = factory.Sequence(lambda n: "slug_%d" % n)
    name = factory.Sequence(lambda n: "name_??????%d" % n)
    slug = factory.Sequence(lambda n: "slug_??????%d" % n) 


class PostTagsFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = PostTags

    author = factory.SubFactory(AuthorFactory)
    name = factory.Sequence(lambda n: "name_??????%d" % n)
    slug = factory.Sequence(lambda n: "slug_??????%d" % n) 


class PostFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Post

    title = factory.Sequence(lambda n: "title_??????%d" % n)
    meta_title = title
    author = factory.SubFactory(AuthorFactory)
    category = factory.SubFactory(CategoryFactory)
    # tags = factory.SubFactory(PostTagsFactory)
    slug = factory.Sequence(lambda n: "slug_??????%d" % n) 
    reading_times = 123
    trending = 34
    summary = fake.text(36)
    content = fake.text(999)
    created_at = factory.LazyFunction(now)
    updated_at = factory.LazyFunction(now)

    @factory.post_generation
    def tags(self, create, extracted, **kwargs):
        # if not create:
        #     # Simple build, do nothing.
        #     return

        if extracted:
            for tag in extracted:
                self.tags.add(tag)


register(AuthorFactory)
register(CategoryFactory)
register(PostTagsFactory)
register(PostFactory)
