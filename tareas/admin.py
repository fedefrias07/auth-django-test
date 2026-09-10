from django.contrib import admin
from tareas.models import Tareas


@admin.register(Tareas)
class TareasAdmin(admin.ModelAdmin):
    # Columnas que se muestran en la lista
    list_display = ("titulo", "descripcion", "completada", "create_at", "usuario")