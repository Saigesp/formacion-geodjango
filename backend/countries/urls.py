from django.urls import path

from . import views

urlpatterns = [
    path("map/", views.map),
    path("map_data/", views.map_data),
]
