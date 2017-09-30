from django.db import models
from common.models import Floor


class StudyRoom(models.Model):
    name = models.CharField(max_length=255)
    status = models.BooleanField()
    floor = models.ForeignKey(Floor, related_name="study_rooms")

    def __str__(self):
        return "{}: {} - {}".format(self.floor, self.name, self.status)
