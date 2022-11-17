import pytest

from apps.authors.models import Author


def test_create_new_author(new_author_factory):
    author = new_author_factory('admin')
    assert str(author) == 'firstname lastname'
