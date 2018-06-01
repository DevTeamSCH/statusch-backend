from django.db import models
from solo.models import SingletonModel


class PrinterProxy(SingletonModel):
    url = models.URLField()
