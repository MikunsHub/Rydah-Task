from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    """
    Custom user model to store user profiles.
    """
    username = models.CharField(
        _("username"),
        max_length=20,
        unique=True,
        null=True,
        blank=False,
        db_index=True,
        validators=[UnicodeUsernameValidator()],
        error_messages={
            "unique": _("That username is not available"),
        },
    )

    email = models.EmailField(
        _("email address"),
        max_length=100,
        unique=True,
        blank=False,
        null=False,
        db_index=True,
        error_messages={
            "unique": _("That email is not available"),
        },
    )
    
    first_name = models.CharField(
        _("first name"), max_length=100, null=False, blank=False
    )
    
    last_name = models.CharField(
        _("last name"), max_length=100, null=False, blank=False
    )


    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = (
        "username",
        "email",
        "first_name",
        "last_name",
    )