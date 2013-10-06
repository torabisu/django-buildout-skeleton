from django.contrib.auth.models import AbstractUser, Group

from pycon.core.models import Base


class EndUser(Base, AbstractUser):
    """
    This EndUser is used instead of the standard django.contrib.auth.models.User.  This allows you
    to connect the standard django user to an additional model like Customer.  You can then use
    request.user.customer in filters etc.
    """

    pass
