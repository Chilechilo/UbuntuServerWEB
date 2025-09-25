from django.shortcuts import render
from django.http import HttpResponse

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