from django.urls import path
from django.conf.urls import include
from django.contrib import admin


urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/v1/", include("laundry_room.urls")),
    path("api/v1/", include("study_room.urls")),
    path("api/v1/", include("printer.urls")),
]
