# inventario/urls.py
from django.urls import path
from . import views


urlpatterns = [
    path('listado', views.lista_productos, name='lista_productos'),
    path('agregar/', views.agregar_producto, name='agregar_producto'),
]