from django.contrib.auth.models import AbstractUser, Group
from django.db import models

from pycon.core.models import Base


class EndUser(Base, AbstractUser):
    """
    This EndUser is used instead of the standard django.contrib.auth.models.User.  Main reason is the link to a
    customer.
    """
    #: User interface skin to use, defaults to "skin-3" (red).
    skin = models.CharField(max_length=16)

    def __str__(self):
        return self.username

