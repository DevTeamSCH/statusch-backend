from rest_framework import serializers
from . import models
from common.models import Floor


class TypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Type
        fields = ("kind_of","name","treshold")

class MachineSerializer(serializers.ModelSerializer):
    type_field = TypeSerializer()

    class Meta:
        model = models.Machine
        fields = ("id", "status", "message","working","type_field")


class FloorSerializer(serializers.ModelSerializer):
    machines = MachineSerializer(many=True)

    class Meta:
        model = Floor
        fields = ("id", "machines", "last_query_time")
