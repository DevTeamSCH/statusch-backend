from rest_framework import serializers
from .models import Machine, Floor


class MachineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Machine
        fields = ('id', 'type', 'status_code', 'message')


class FloorSerializer(serializers.ModelSerializer):
    machines = MachineSerializer(many=True)

    class Meta:
        model = Floor
        fields = ('id', 'machines', 'last_query_time')
