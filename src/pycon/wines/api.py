import logging

from rest_framework import viewsets, serializers

from pycon.wines.models import Wine


logger = logging.getLogger(__name__)


class WineSerializer(serializers.ModelSerializer):

    class Meta:
        model = Wine
        fields = ('id', 'name')


class WineViewSet(viewsets.ModelViewSet):
    model = Wine
    serializer_class = WineSerializer
