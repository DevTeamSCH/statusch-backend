from rest_framework.routers import DefaultRouter

from .apps import LaundryRoomConfig
from . import views

router = DefaultRouter()
router.register(r'laundry-room', views.FloorViewSet)
router.register(r'alerts', views.AlertViewSet)

app_name = LaundryRoomConfig.name
urlpatterns = router.urls
