from django.shortcuts import render, redirect
from .models import Tareas
from django.contrib import messages
from django.contrib.auth.decorators import login_required
import re

@login_required
def tareas(request):

    lista = Tareas.objects.filter(usuario=request.user)

    return render(request, "tareas/tareas.html", {"lista": lista})

@login_required
def crear_tarea(request):

    if request.method == "POST":

        titulo = request.POST.get("titulo", "").strip()

        if not titulo:
            messages.warning(request, "El título no puede estar vacío")
        elif not re.match(r"^[a-zA-Z0-9áéíóúÁÉÍÓÚñÑ\s]+$", titulo):
            messages.warning(request, "Caracteres no permitidos")
        elif len(titulo) > 40:
            messages.warning(request, "Supero el limite de caracteres")
        else:
            Tareas.objects.create(titulo=titulo,usuario=request.user)
            messages.success(request, "Tarea creada.")
            return redirect("tareas")

    return render(request, "tareas/crear-tarea.html")

@login_required
def cambiar_estado(request, id):
    tarea = Tareas.objects.get(id=id)

    tarea.completada = not tarea.completada
    tarea.save()

    return redirect("tareas")


@login_required
def eliminar_tarea(request, id):
    tarea = Tareas.objects.get(id=id)

    tarea.delete()

    return redirect("tareas")

