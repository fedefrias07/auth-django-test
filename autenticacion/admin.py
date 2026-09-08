from django.contrib import admin
from autenticacion.models import UsuarioCustom
# Register your models here.

admin.site.site_header = "Auth — Panel de Administración"
admin.site.site_title = "Auth test"
admin.site.index_title = "Administracion"


@admin.register(UsuarioCustom)
class UsuarioAdmin(admin.ModelAdmin):

    # Columnas que se muestran en la lista
    list_display = ("first_name", "last_name", "email")

    

