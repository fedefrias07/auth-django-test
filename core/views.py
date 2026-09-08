from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render, redirect
from .forms import DatosPersonalesForm

def home (request):
    return render(request, "core/index.html")

def contacto (request):
    return render(request, "core/contacto.html")

@login_required
def cuenta(request):
    if request.method == "POST":
        form = DatosPersonalesForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, "Datos actualizados.")
            return redirect("cuenta")
    else:
        form = DatosPersonalesForm(instance=request.user)

    return render(request, "core/cuenta.html", {"form": form})
