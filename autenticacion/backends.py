# Para un proyecto normal donde solo querés email + contraseña, con USERNAME_FIELD = "email" alcanza y backends.py sobra. Lo que está en la guía es para cuando el proyecto crece y necesitás ese control extra.

# Usarías backends.py en estos casos concretos:

# 1. Login con email O username al mismo tiempo
# user = User.objects.get(Q(email=valor) | Q(username=valor))

# 2. Bloqueo por intentos fallidos
# if intentos_fallidos(email) >= 5:
#     return None  # bloqueado

# 3. Autenticar contra algo externo
# LDAP, Active Directory, una API de terceros, etc.
# respuesta = ldap.autenticar(email, password)

# 4. Lógica extra al autenticar
# registrar logs, actualizar último intento, 2FA, etc.

from django.contrib.auth.backends import BaseBackend
from django.contrib.auth import get_user_model


User = get_user_model()

class EmailBackend(BaseBackend):

    def authenticate(self, request, email=None, password=None, **kwargs):
        if email is None:
            email = kwargs.get("username")
        if email is None or password is None:
            return None

        try:
            user = User.objects.get(email=email.lower())
        except User.DoesNotExist:
            User().check_password(password)  # evita timing attacks
            return None


        if user.check_password(password) and self.user_can_authenticate(user):
            return user
        return None


    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None

    def user_can_authenticate(self, user):
        return getattr(user, "is_active", False)
