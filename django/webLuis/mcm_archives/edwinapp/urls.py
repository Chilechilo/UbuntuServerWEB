from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("index1", views.index1, name="index1"),
    path("index2", views.index1, name="index2"),
    path("about/", views.aboutp, name="about"),
    path("sumar/", views.sumar, name="sumar"),
    path("<str:nombre>", views.saludo, name="saludo"),
]
