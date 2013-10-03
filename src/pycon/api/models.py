import logging

from django.db import models


logger = logging.getLogger(__name__)


class DataPoint(models.Model):
    """
    Handles the structure of a point when pulling reports and displaying them through a JavaScript graphing library
    like HighCharts.
    """
    #: Human friendly label identifying the point
    label = models.CharField(max_length=255)
    #: Stored value
    value = models.FloatField()

    class Meta:
        managed = False
