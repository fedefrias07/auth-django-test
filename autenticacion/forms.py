from django import forms
from django.contrib.auth import authenticate, get_user_model
from django.contrib.auth.forms import UserCreationForm


User = get_user_model()


class LoginForm(forms.Form):
    email    = forms.EmailField(label="Email")
    password = forms.CharField(label="Contraseña", widget=forms.PasswordInput)


    def clean(self):
        cleaned  = super().clean()
        email    = cleaned.get("email", "").lower()
        password = cleaned.get("password")


        if email and password:
            self.user = authenticate(email=email, password=password)
            if self.user is None:
                raise forms.ValidationError("Email o contraseña incorrectos.")
            if not self.user.is_active:
                raise forms.ValidationError("Esta cuenta está desactivada.")
        return cleaned


    def get_user(self):
        return getattr(self, "user", None)


class RegisterForm(UserCreationForm):
    email      = forms.EmailField(label="Email")
    first_name = forms.CharField(label="Nombre", max_length=150, required=False)
    last_name  = forms.CharField(label="Apellido", max_length=150, required=False)


    class Meta:
        model  = User
        fields = ("email", "first_name", "last_name", "password1", "password2")


    def clean_email(self):
        email = self.cleaned_data["email"].lower()
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Ya existe una cuenta con este email.")
        return email
