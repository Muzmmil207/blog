from django.contrib.auth.models import AbstractUser, PermissionsMixin
from django.core.validators import RegexValidator
from django.db import models
from django.utils.timezone import now
from django.utils.translation import gettext_lazy as _


class Author(AbstractUser):
    """ Customize default User model """
    first_name = models.CharField(
        max_length=50,
        verbose_name=_("Author Name"),
        help_text=_("format: required, max-50"),
    )
    middle_name = models.CharField(
        max_length=50,
        blank=True,
        verbose_name=_("Author Middle Name"),
        help_text=_("format: required, max-50"),
    )
    last_name = models.CharField(
        max_length=50,
        verbose_name=_("Author Last Name"),
        help_text=_("format: required, max-50"),
    )
    email = models.EmailField(
        unique=True,
        verbose_name=_("E-mail"),
        error_messages={
            "unique": "Please use another Email, this is already exists.",
        },
    )
    phone_regex = RegexValidator(
        regex=r"^(?:\+249|0)?(01\d{8})$",
        message=_("Phone number must be entered in the format: `+24901XXXXXXXX`.")
    )
    mobile_number = models.CharField(
        validators=[phone_regex],
        max_length=20,
        unique=True,
        verbose_name=_("Mobile Number"),
    )
    last_activity = models.DateTimeField(
        verbose_name=_("Last activity"),
        blank=True,
        null=True,
    )
    created_at = models.DateTimeField(default=now, editable=False)
    about = models.TextField(
        max_length=1500,
        blank=True,
        null=True,
        verbose_name=_("About"),
        help_text=_("Description about the author"),
    )
    def __str__(self):
        return f"{self.first_name} {self.last_name}"
