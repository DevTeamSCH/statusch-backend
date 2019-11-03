from rest_framework import serializers
from . import models
from common.models import Floor


class MachineSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Machine
        fields = ("id", "kind_of", "status", "message")


class FloorSerializer(serializers.ModelSerializer):
    machines = serializers.SerializerMethodField()

    class Meta:
        model = Floor
        fields = ("id", "machines", "last_query_time")

    def get_machines(self, instance):
        machines = instance.machines.exclude(status=2).order_by("kind_of")
        return MachineSerializer(machines, many=True).data
