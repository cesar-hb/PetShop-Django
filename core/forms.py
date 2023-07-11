from django import forms
from django.forms import ModelForm, fields, Form
from .models import Producto, PerfilUsuario,Bodega
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

form_control = {'class': 'form-control'}
form_file = {'class': 'form-control-file', 'title': 'Debe subir una imagen'}
form_text_area = {'class': 'form-control', 'rows': '3'}

class ProductoForm(ModelForm):
    class Meta:
        model = Producto
        fields = ['id', 'nombre', 'descripcion', 'precio', 
        'descuento_sub', 'descuento_oferta', 'imagen', 'categoria']

class IniciarSesionForm(Form):
    username = forms.CharField(widget=forms.TextInput(), label="Nombre de Usuario")
    password = forms.CharField(widget=forms.PasswordInput(), label="Contraseña")
    class Meta:
        fields = ['username', 'password']


class RegistroForm(UserCreationForm):
    subscripcion = forms.BooleanField()
    rut = forms.CharField(max_length=15, required=True, widget=forms.TextInput)
    direccion = forms.CharField(max_length=400, required=True,widget=forms.Textarea,)
    imagen = forms.CharField(required=True,widget=forms.FileInput(attrs=form_file),)
    class Meta:
        model = User
        fields = [
                'username',
                'rut',
                'first_name',
                'last_name',
                'email',
                'subscripcion',
                'direccion',
                'imagen',   
            ]
        labels = {
                'username': 'Nombre de usuario',
                'rut': 'Rut',
                'first_name': 'Nombre',
                'last_name': 'Apellidos',
                'email': 'Correo',
                'subscripcion': 'Subscripción',
                'direccion': 'Dirección',
                'imagen': 'Imagen',
        }



#class Bodega(forms.Form):

#    categoria = forms.ModelChoiceField(
#        queryset=Categoria.objects.all(),
#        widget=forms.Select(attrs=form_select),
#        label='Categoría'
#    )
#    producto = forms.ModelChoiceField(
#        queryset=Producto.objects.none(), 
#        widget=forms.Select(attrs=form_select),
#        label='Producto'
#    )
#    cantidad = forms.IntegerField(
#        widget=forms.NumberInput(attrs=form_control),
#        label='Cantidad'
#    )

#    class Meta:
#        fields = '__all__'