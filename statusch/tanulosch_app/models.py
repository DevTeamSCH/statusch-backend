from django.db import models

# Create your models here.
from django.db import models


class Floor(models.Model):
    id = models.IntegerField(unique=True, primary_key=True)

    def __str__(self):
        return "Floor %s" % self.id


class LearningRoom(models.Model):
    name = models.CharField(max_length=255)
    status = models.BooleanField()
    floor = models.ForeignKey(Floor, related_name="learning_rooms")

    def __str__(self):
        return "{}: {} - {}".format(self.floor, self.name, self.status)
