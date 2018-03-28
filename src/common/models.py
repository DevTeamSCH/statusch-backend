from django.db import models


class Floor(models.Model):
    id = models.IntegerField(unique=True, primary_key=True)
    ip_addr = models.CharField(max_length=255)
    last_query_time = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return "Floor {}".format(self.id)
