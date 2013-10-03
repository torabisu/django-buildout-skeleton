from pycon.core.models import Base

from django.db import models


class Wine(Base):
    """
    Store different varietals
    """
    #: Name of the wine.
    name = models.CharField(max_length=128, default='')


class WhiteWine(Wine):
    """
    Handles all white wines
    """
    pass


class RedWine(Wine):
    pass


class SavignonBlanc(WhiteWine):

    def is_green(self):
        """

        """
        return True


class Merlot(RedWine):
    pass