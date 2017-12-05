from django.conf.urls import url, include
from django.contrib import admin

import django_eventstream

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/v1/laundry-room/', include('laundry_room.urls')),
    url(r'^api/v1/study-room/', include('study_room.urls')),
    url(r'^events/', include(django_eventstream.urls)),
]
