from django.urls import path
from . import views

urlpatterns = [
    path("", views.root_view),
    path("health", views.health_view),
]
