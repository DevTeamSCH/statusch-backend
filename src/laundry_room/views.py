from rest_framework import viewsets
from datetime import datetime

from common.models import Floor, Alert
from common.serializers import AlertSerializer
from . import serializers

class FloorViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = serializers.FloorSerializer
    queryset = Floor.objects.exclude(machines__isnull=True).order_by('id')

class AlertViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = AlertSerializer
    queryset = Alert.objects.exclude(expires__gt=datetime.now()).order_by('id')
