from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Task
from django.urls import reverse

# Create your views here.

def index(request):
    return HttpResponse("Hello, world!")

def saludo (request, nombre):
    return render(request, "edwinapp/saludo.html", {
        "nombre":nombre.capitalize()
        })

def index1 (request):
    return render(request, "edwinapp/index.html")

def aboutp (request):
    return render(request, "edwinapp/about.html")

def sumar(request):
    a = request.GET.get("a")
    b = request.GET.get("b")
    resultado = None
    error = None

    if a is not None and b is not None:
        try:
            resultado = float(a) + float(b)
        except ValueError:
            error = "Ingresa números válidos."

    return render(request, "edwinapp/sumar.html", {
        "a": a or "",
        "b": b or "",
        "resultado": resultado,
        "error": error,
    })

tasks = ["foo","bar","baz"]

def tasks_index(request):
    return render (request, "edwinapp/tasks_index.html", {
        "tasks": tasks
    })

def tasks_add (request):
    if request.method == "POST":
        task = request.POST.get ("task")
        if task:
            task.append(task)
        return HttpResponseRedirect(reverse("task_index"))
    return render(request,"edwinapp/tasks_add.html")

def tasks_admin_list(request):
    task = Task.objects.all().order_by("_created_at")
    return render(request, "edwinapp/tasks_admin_list.html", {
        "tasks":task
    })

def index2(request):
    return HttpResponse("Bienvenido al menú")
