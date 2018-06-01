from django.contrib import admin
from solo.admin import SingletonModelAdmin

from . import models


admin.site.register(models.PrinterProxy, SingletonModelAdmin)
