from django.conf.urls import url, include
from django.contrib import admin
from .api_urls import api_router_washing, api_router_learning

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^washing_api/', include(api_router_washing.urls)),
    url(r'^learning_api/', include(api_router_learning.urls)),
]
