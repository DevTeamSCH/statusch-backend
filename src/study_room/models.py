from django.db import models
from common.models import Floor


class StudyRoom(models.Model):
    STATUS_CHOICES = (
        (0, "Free"),
        (1, "Busy"),
        (2, "N/A"),
    )

    name = models.CharField(max_length=255)
    status = models.IntegerField(blank=True, choices=STATUS_CHOICES, null=True)
    floor = models.ForeignKey(Floor, related_name="study_rooms")

    def __str__(self):
        return "{}: {} - {}".format(self.floor, self.name, self.status)
