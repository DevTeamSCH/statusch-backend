from rest_framework.routers import DefaultRouter

from .apps import LaundryRoomConfig
from . import views

router = DefaultRouter()
router.register(r'', views.FloorViewSet)

app_name = LaundryRoomConfig.name
urlpatterns = router.urls
