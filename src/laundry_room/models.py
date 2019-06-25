from django.db import models
from common.models import Floor


class Type(models.Model):
    TYPE_CHOICES = (("WM", "WashingMachine"), ("DR", "Dryer"))

    kind_of = models.CharField(max_length=2, choices=TYPE_CHOICES)
    name = models.CharField(max_length = 125)
    treshhold = models.IntegerField()


class Machine(models.Model):
    STATUS_CHOICES = ((0, "Free"), (1, "Busy"), (2, "N/A"))

    status = models.IntegerField(blank=True, choices=STATUS_CHOICES, null=True)
    message = models.CharField(blank=True, null=True, max_length=255)
    floor = models.ForeignKey(
        Floor, related_name="machines", on_delete=models.DO_NOTHING
    )
    type = models.ForeignKey(
        Type, related_name="machines", on_delete=models.DO_NOTHING
    )
    working = models.BooleanField(default=True)

    def __str__(self):
        return "{} {}".format(self.floor, self.type)


class Value(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True, editable=False)
    value = models.IntegerField()
    machine = models.ForeignKey(
        Machine, related_name="values", on_delete=models.DO_NOTHING
    )
