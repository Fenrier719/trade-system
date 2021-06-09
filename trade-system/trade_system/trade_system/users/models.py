from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models import CharField
from django.urls import reverse

from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    """Default user for trade_system."""

    #: First and last name do not cover name patterns around the globe
    name = CharField(_("Name of User"), blank=True, max_length=255)
    first_name = None  # type: ignore
    last_name = None  # type: ignore
    deposit = models.DecimalField(max_digits=8, decimal_places=2, default=1000)

