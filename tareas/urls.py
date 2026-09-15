from django.urls import path
from tareas.views import tareas, crear_tarea, cambiar_estado, eliminar_tarea


urlpatterns = [
    path('lista', tareas, name="tareas"),
    path('crear-tarea', crear_tarea, name="crear_tarea"),
    path("cambiar-estado/<int:id>/", cambiar_estado, name="cambiar_estado"),
    path("eliminar-tarea/<int:id>/", eliminar_tarea, name="eliminar_tarea"),

]