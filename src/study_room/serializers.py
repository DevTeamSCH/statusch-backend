from rest_framework import serializers
from . import models
from common.models import Floor


class StudyRoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.StudyRoom
        fields = ("id", "name", "status")


class FloorSerializer(serializers.ModelSerializer):
    study_rooms = StudyRoomSerializer(many=True)

    class Meta:
        model = Floor
        fields = ("id", "study_rooms", "last_query_time")
