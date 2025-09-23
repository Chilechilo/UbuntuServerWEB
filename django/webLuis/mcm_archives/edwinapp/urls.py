from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<str:nombre>", views.saludo, name="saludo"),
    path("index1", views.index1, name="index"),
]
