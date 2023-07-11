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
    descuento_oferta = models.CharField(max_length=3, blank=True, null=True, verbose_name="Descuento oferta")
    imagen = models.ImageField(upload_to="images/", default="sinfoto.jpg", null=False, blank=False, verbose_name="Imagen")
    categoria = models.ForeignKey(Categoria, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.id

#Create perfil usuario
class Bodega(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.DO_NOTHING, verbose_name='Producto')
    def __str__(self):
        consulta_sql = f'SELECT boleta_id FROM DetalleBoleta WHERE bodega_id={self.id}'
        with connection.cursor() as cursor:
            cursor.execute(consulta_sql)
            resultado = cursor.fetchone()
        info = f'Vendido (Boleta {resultado[0]})' if resultado else 'En bodega'
        return f'{self.producto.nombre} (ID {self.id}) - {info}'
    
    def acciones():
        return {
            'accion_eliminar': 'eliminar el producto de la Bodega',
            'accion_actualizar': 'actualizar el producto de la Bodega'
        }

class PerfilUsuario(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    rut = models.CharField(max_length=15, blank=False, null=False, verbose_name="Rut")
    direccion = models.CharField(max_length=150, blank=False, null=False, verbose_name="Dirección")
    subscripcion = models.BooleanField()
    imagen = models.ImageField(upload_to='imagen_perfil/', blank=False, null=False, verbose_name='Imagen')
    def __str__(self):
        
        return f"{self.user.first_name} {self.user.last_name} ({self.user.email}) {self.user.subscripcion} {self.user.rut} {self.user.direccion}"
    def acciones():
        return {
            'accion_eliminar': 'eliminar el Perfil',
            'accion_actualizar': 'actualizar el Perfil'
        }
