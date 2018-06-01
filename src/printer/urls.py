from django.urls import path

from . import views


urlpatterns = [
    path('printer', views.PrintersByUsers.as_view()),
]
