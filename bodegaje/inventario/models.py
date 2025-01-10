# inventario/models.py
from django.db import models

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    cantidad = models.IntegerField()
    descripcion = models.TextField()
    fecha_ingreso = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.nombre
    
    
# Create your models here.