from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# Create modelo categoria

class Categoria(models.Model):
    idCategoria = models.IntegerField(primary_key=True, verbose_name="Id de categoría")
    nombreCategoria = models.CharField(max_length=80, blank=False, null=False, verbose_name="Nombre de la categoría")

def __str__(self):
    return f"{self.idCategoria} - {self.nombreCategoria}"

# Create Modelo para producto

class Producto(models.Model):
    id = models.IntegerField(primary_key=True, verbose_name="ID")
    nombre = models.CharField(max_length=80, blank=False, null=False, verbose_name="Nombre")
    descripcion = models.CharField(max_length=200, null=True, blank=True, verbose_name="Descripción")
    precio = models.CharField(max_length=10, blank=False, null=False, verbose_name="Precio")
    descuento_sub = models.CharField(max_length=3, blank=False, null=False, verbose_name="Descuento subscriptor")
    descuento_oferta = models.CharField(max_length=3, blank=True, null=True, verbose_name="Nombre")
    imagen = models.ImageField(upload_to="images/", default="sinfoto.jpg", null=False, blank=False, verbose_name="Imagen")
    categoria = models.ForeignKey(Categoria, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.id

#Create perfil usuario

class PerfilUsuario(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    rut = models.CharField(max_length=80, blank=True, null=True, verbose_name="Rut")
    direccion = models.CharField(max_length=80, blank=True, null=True, verbose_name="Dirección")

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name} ({self.user.email})"