from django.urls import path
from core.views import home, contacto, cuenta

urlpatterns = [
    path('', home, name="index"),
    path('contacto', contacto, name="contacto"),
    path('cuenta', cuenta, name="cuenta"),
]