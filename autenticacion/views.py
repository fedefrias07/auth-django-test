from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages
from .forms import LoginForm, RegisterForm


def login_view(request):
    if request.user.is_authenticated:
        return redirect("/")
    form = LoginForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        login(request, form.get_user())
        return redirect(request.GET.get("next", "/"))
    return render(request, "autenticacion/login.html", {"form": form})

def register_view(request):
    form = RegisterForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        user = form.save()
        # Cuando logea sin esto como parametro en el login(), directamente va a la vista del home
        # backend="autenticacion.backends.EmailBackend"
        login(request, user)
        return redirect("autenticacion:login")
    return render(request, "autenticacion/register.html", {"form": form})

def logout_view(request):
    logout(request)
    return redirect("autenticacion:login")

@login_required
def cambiar_contrasena(request):
    if request.method == "POST":
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            usuario = form.save()
            update_session_auth_hash(request, usuario)
            messages.success(request, "Contraseña cambiada correctamente.")
            return redirect("/")
    else:
        form = PasswordChangeForm(request.user)
    return render(request, "autenticacion/cambiar-contrasena.html", {"form": form})
