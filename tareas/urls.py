from django.urls import path
from tareas.views import tareas, crear_tarea


urlpatterns = [
    path('lista', tareas, name="tareas"),
    path('crear-tarea', crear_tarea, name="crear_tarea"),
]