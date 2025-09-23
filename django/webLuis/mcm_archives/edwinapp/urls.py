from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path('suma/', views.suma, name='suma'),
    path('suma/<int:a>/<int:b>/', views.suma_path, name='suma_path'),
    path('pagina/', views.pagina, name='pagina')
]
