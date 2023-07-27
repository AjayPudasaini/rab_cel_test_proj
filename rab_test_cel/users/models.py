from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from rab_test_cel.utils.models import AbstractDateTime
from rab_test_cel.users.managers import CustomUserManager


class User(AbstractUser, AbstractDateTime):
    """
    Default custom user model for rab_test_cel.
    If adding fields that need to be filled at user signup,
    check forms.SignupForm and forms.SocialSignupForms accordingly.
    """

    # First and last name do not cover name patterns around the globe
    name = models.CharField(_("Name of User"), blank=True, max_length=255)
    first_name = None  # type: ignore
    last_name = None  # type: ignore
    email = models.EmailField(_("email address"), unique=True)
    is_admin = models.BooleanField(_("Is Admin"), default=False)
    is_customer = models.BooleanField(_("Is Customer"), default=False)
    username = None  # type: ignore

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()


    class Meta:
        db_table="User"