from rest_framework.routers import DefaultRouter
import mosogepsch_app.views as views

api_router = DefaultRouter()
api_router.register(
    'floors', views.FloorViewSet, base_name='floor'
)
