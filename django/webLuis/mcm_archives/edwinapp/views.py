from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("Hello, world!")

def suma(request):
    a = request.GET.get("a")
    b = request.GET.get("b")
    if a is None or b is None:
        return HttpResponse("Faltan parámetros. Usa ?a=<num>&b=<num>", status=400)
    try:
        a = float(a); b = float(b)
    except ValueError:
        return HttpResponse("a y b deben ser números.", status=400)
    return HttpResponse(f"Resultado: {a} + {b} = {a+b}")

# /edwinapp/suma/3/7/
def suma_path(request, a, b):
    res = a + b
    return HttpResponse(f"Resultado: {a} + {b} = {res}")

# /edwinapp/pagina/
def pagina(request):
    return HttpResponse(
        "<!doctype html><html><head><meta charset='utf-8'><title>Página</title></head>"
        "<body style='font-family:system-ui;background:#111;color:#eee'>"
        "<h1>¡Hola desde HTML!</h1><p>Vista HTML simple.</p>"
        "<a href='/edwinapp/suma/5/7/' style='color:#8ab4f8'>Probar suma 5+7</a>"
        "</body></html>",
        content_type="text/html"
    )
