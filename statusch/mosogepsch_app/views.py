from rest_framework import viewsets
from . import serializers
from . import models


class FloorViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = serializers.FloorSerializer
    queryset = models.Floor.objects.exclude(machines__isnull=True)
