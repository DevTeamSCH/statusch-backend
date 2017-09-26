from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from rest_framework.generics import mixins
from . import serializers
from . import models


class FloorViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = serializers.FloorSerializer
    queryset = models.Floor.objects.all()

class LearningRoomViewSet(viewsets.GenericViewSet, mixins.UpdateModelMixin):
    serializer_class = serializers.LearningRoomSerializer
    queryset = models.LearningRoom.objects.all()
