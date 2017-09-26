from django.db import models


class Floor(models.Model):
    id = models.IntegerField(unique=True, primary_key=True)
    ip_addr = models.CharField(max_length=255)
    last_query_time = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return "Floor %s" % self.id


class Machine(models.Model):
    TYPE_CHOICES = (
        ("WM", "WashingMachine"),
        ("DR", "Dryer")
    )
    STATUS_CHOICES = (
        (0, "Free"),
        (1, "Busy"),
        (2, "N/A")
    )
    type = models.CharField(max_length=2, choices=TYPE_CHOICES)

    status_code = models.IntegerField(blank=True, choices=STATUS_CHOICES, null=True)
    message = models.CharField(blank=True, null=True, max_length=255)
    floor = models.ForeignKey(Floor, related_name="machines")

    def __str__(self):
        return "{} {}".format(self.floor, self.type)
