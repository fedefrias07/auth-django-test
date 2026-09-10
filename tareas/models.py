from django.db import models
from django.conf import settings


class Tareas(models.Model):
    titulo = models.CharField(max_length=40, blank=False)
    descripcion = models.CharField(max_length=300, blank=True, null=True)
    completada = models.BooleanField(default=False)
    create_at = models.DateTimeField(auto_now_add=True)
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name="Persona")
    



