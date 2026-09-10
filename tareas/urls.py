from django.urls import path
from tareas.views import tareas


urlpatterns = [
    path('lista', tareas, name="tareas"),
]