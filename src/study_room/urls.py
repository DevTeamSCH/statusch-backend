from rest_framework.routers import DefaultRouter

from .apps import StudyRoomConfig
from . import views

router = DefaultRouter()
router.register(r"study-room", views.FloorViewSet)

app_name = StudyRoomConfig.name
urlpatterns = router.urls
