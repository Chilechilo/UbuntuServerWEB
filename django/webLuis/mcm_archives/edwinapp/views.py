from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("Hello, world!")

def saludo (request, nombre):
    return render(request, "edwinapp/saludo.html", {
        "nombre":nombre.capitalize()
        })
