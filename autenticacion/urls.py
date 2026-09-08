from django.urls import path
from autenticacion.views import login_view, register_view, cambiar_contrasena, logout_view

app_name = 'autenticacion'

urlpatterns = [
    path('login', login_view, name='login'),
    path('register', register_view, name='register'),
    path('logout', logout_view, name='logout'),
    path('cambiar-password', cambiar_contrasena, name='cambiar-password'),
]
