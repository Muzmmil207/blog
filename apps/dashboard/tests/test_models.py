import pytest

from apps.dashboard.models import Category


@pytest.mark.xfail
@pytest.mark.parametrize(
    "id, name, slug",
    [
        (1, "fashion", "fashion"),
        (18, "trainers", "trainers"),
        (35, "baseball", "baseball"),
    ],
)
def test_category(db, db_fixture_setup, id, name, slug):
    cat = Category.objects.get(id=id)
    print(cat.name)
    assert cat.name == name
    assert cat.slug == slug
    assert str(cat) == name


@pytest.mark.parametrize(
    "name, slug",
    [
        ("fashion", "fashion"),
        ("trainers", "trainers"),
        ("baseball", "baseball"),
    ],
)
def test_category_insert_data(db, category_factory, name, slug):
    cat = category_factory.create(name=name, slug=slug)
    assert cat.name == name
    assert cat.slug == slug
    assert str(cat) == name
