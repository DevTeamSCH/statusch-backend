from rest_framework.routers import DefaultRouter
import mosogepsch_app.views as mosogepsch_app_views
import tanulosch_app.views as tanulosch_app_views

api_router_mosogepsch = DefaultRouter()
api_router_mosogepsch.register(
    'floors', mosogepsch_app_views.FloorViewSet, base_name='floor'
)

api_router_tanulosch = DefaultRouter()
api_router_tanulosch.register(
    'floors', tanulosch_app_views.FloorViewSet, base_name='floor'
)

api_router_tanulosch.register(
    'learning_rooms', tanulosch_app_views.LearningRoomViewSet, base_name='learning_room'
 )
