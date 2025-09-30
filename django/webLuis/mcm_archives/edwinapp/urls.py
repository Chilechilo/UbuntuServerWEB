from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("index1", views.index1, name="index1"),
    path("about/", views.aboutp, name="about"),
    path("sumar/", views.sumar, name="sumar"),
    path("<str:nombre>", views.saludo, name="saludo"),
    path("tasks", views.tasks_index, name="tasks_index"),
    path("tasks/add", views.tasks_add, name="tasks_add"),
    path("admin_tasks", views.tasks_admin_list, name="tasks_admin_list"),
    path("menu", views.index2, name="index2")
]
