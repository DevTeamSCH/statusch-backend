from rest_framework import serializers
from . import models
from common.models import Floor


class MachineSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Machine
        fields = ("id", "kind_of", "status", "message")


class FloorSerializer(serializers.ModelSerializer):
    machines = MachineSerializer(many=True)

    class Meta:
        model = Floor
        fields = ("id", "machines", "last_query_time")
