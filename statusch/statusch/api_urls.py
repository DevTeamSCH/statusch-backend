from rest_framework.routers import DefaultRouter
import washing_app.views as washing_app_views
import learning_app.views as learning_app_views

api_router_washing = DefaultRouter()
api_router_washing.register(
    'floors', washing_app_views.FloorViewSet, base_name='floor'
)

api_router_learning = DefaultRouter()
api_router_learning.register(
    'floors', learning_app_views.FloorViewSet, base_name='floor'
)

api_router_learning.register(
    'learning_rooms', learning_app_views.LearningRoomViewSet, base_name='learning_room'
 )
