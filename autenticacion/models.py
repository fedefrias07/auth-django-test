from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin


class UsuarioCustomManager(BaseUserManager):

    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("El email es obligatorio")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)  # hashea la contraseña
        user.save(using=self._db)
        return user


    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)
        return self.create_user(email, password, **extra_fields)


class UsuarioCustom(AbstractBaseUser, PermissionsMixin):
    email       = models.EmailField(unique=True)
    first_name  = models.CharField(max_length=150, blank=True, verbose_name="Nombre")
    last_name   = models.CharField(max_length=150, blank=True, verbose_name="Apellido")
    avatar = models.ImageField(upload_to="avatars/", blank=True, null=True, verbose_name="Foto de perfil")
    is_active   = models.BooleanField(default=True)
    is_staff    = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=True)


    objects = UsuarioCustomManager()

    # USERNAME_FIELD le dice a Django cuál es el campo identificador único del usuario — es decir, el campo que se usa para hacer login.
    USERNAME_FIELD  = "email"
    REQUIRED_FIELDS = []


    class Meta:
        verbose_name = "usuario"
        verbose_name_plural = "usuarios"


    def __str__(self):
        return self.email

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}".strip()
