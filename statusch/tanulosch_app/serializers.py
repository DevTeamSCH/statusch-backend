from rest_framework import serializers
from .models import LearningRoom, Floor


class LearningRoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = LearningRoom
        fields = ('id', 'name', 'status')


class FloorSerializer(serializers.ModelSerializer):
    learning_rooms = LearningRoomSerializer(many=True)

    class Meta:
        model = Floor
        fields = ('id', 'learning_rooms')
