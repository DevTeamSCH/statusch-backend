from django.db import models
from common.models import Floor


class Machine(models.Model):
    TYPE_CHOICES = (
        ("WM", "WashingMachine"),
        ("DR", "Dryer"),
    )
    STATUS_CHOICES = (
        (0, "Free"),
        (1, "Busy"),
        (2, "N/A"),
    )

    kind_of = models.CharField(max_length=2, choices=TYPE_CHOICES)
    status = models.IntegerField(blank=True, choices=STATUS_CHOICES, null=True)
    message = models.CharField(blank=True, null=True, max_length=255)
    floor = models.ForeignKey(Floor, related_name="machines", on_delete=models.DO_NOTHING)

    def __str__(self):
        return "{} {}".format(self.floor, self.kind_of)
