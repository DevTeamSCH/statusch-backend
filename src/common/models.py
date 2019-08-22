from django.db import models


class Floor(models.Model):
    id = models.IntegerField(unique=True, primary_key=True)
    ip_addr = models.CharField(max_length=255)
    last_query_time = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return "Floor {}".format(self.id)

class Alert(models.Model):
    id = models.IntegerField(unique=True, primary_key=True)
    text = models.CharField(max_length=1000)
    level = models.IntegerField() # 0=info, 1=warn, 2=error, 3=critical
    expires = models.DateTimeField()
    
    def __str__(self):
        return self.text
