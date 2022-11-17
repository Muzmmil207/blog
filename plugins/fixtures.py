import pytest

from apps.authors.models import Author
from django.core.management import call_command


@pytest.fixture
def new_author_factory(db):
    def create_author(
        username: str,
        password: str = None,
        first_name: str = "firstname",
        last_name: str = "lastname",
        email: str = "test@test.com",
        mobile_number: str = "+2490113336724",
        is_staff: str = False,
        is_superuser: str = False,
        is_active: str = True,
    ):
        user = Author.objects.create_user(
            username=username,
            password=password,
            first_name=first_name,
            last_name=last_name,
            email=email,
            mobile_number=mobile_number,
            is_staff=is_staff,
            is_superuser=is_superuser,
            is_active=is_active,
        )
        return user
    return create_author


@pytest.fixture(scope="session")
def db_fixture_setup(django_db_setup, django_db_blocker):
    """
    Load DB data fixtures
    """
    with django_db_blocker.unblock():
        call_command("loaddata", "db_authors_fixture.json")
        call_command("loaddata", "db_category_fixture.json")
        call_command("loaddata", "db_tags_fixture.json")
        call_command("loaddata", "db_post_fixture.json")

