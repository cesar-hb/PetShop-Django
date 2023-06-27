from django.shortcuts import redirect, render
from .models import Producto, Categoria
from .forms import ProductoForm, IniciarSesionForm, RegistroForm
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.contrib.auth import login, logout, authenticate

# Create your views here.


def home(request):
    return render(request, "core/home.html")

def iniciar_sesion(request):
    data = {"mesg": "", "form": IniciarSesionForm()}

    if request.method == "POST":
        form = IniciarSesionForm(request.POST)
        if form.is_valid:
            username = request.POST.get("username")
            password = request.POST.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect(home)
                else:
                    data["mesg"] = "¡La cuenta o la password no son correctos!"
            else:
                data["mesg"] = "¡La cuenta o la password no son correctos!"
    return render(request, "core/iniciar_sesion.html", data)

def cerrar_sesion(request):
    logout(request)
    return redirect(home)

class registrar_usuario(CreateView):
    model = User
    template_name = "core/registrar_usuario.html"
    form_class = RegistroForm
    success_url = reverse_lazy('iniciar_sesion')
       
def producto_tienda(request):
    data = {"list": Producto.objects.all().order_by('id')}
    return render(request, "core/producto_tienda.html", data)


def producto_ficha(request, id):
    producto = Producto.objects.get(id=id)
    data = {"producto":  producto}
    return render(request, "core/producto_ficha.html", data)


def producto(request, action, id):
    data = {"mesg": "", "form": ProductoForm, "action": action, "id": id}


    if action == 'ins':
        if request.method == "POST":
            form = ProductoForm(request.POST, request.FILES)
            if form.is_valid:
                try:
                    form.save()
                    data["mesg"] = "¡El producto fue creado correctamente!"
                except:
                    data["mesg"] = "¡No se puede crear dos productos con la misma ID!"


    elif action == 'upd':
        objeto = Producto.objects.get(id=id)
        if request.method == "POST":
            form = ProductoForm(data=request.POST, files=request.FILES, instance=objeto)
            if form.is_valid:
                form.save()
                data["mesg"] = "¡El producto fue actualizado correctamente!"
        data["form"] = ProductoForm(instance=objeto)


    elif action == 'del':
        try:
            Producto.objects.get(id=id).delete()
            data["mesg"] = "¡El producto fue eliminado correctamente!"
            return redirect(producto, action='ins', id = '-1')
        except:
            data["mesg"] = "¡El producto ya estaba eliminado!"


    data["list"] = Producto.objects.all().order_by('id')
    return render(request, "core/producto.html", data)

def ropa(request):
    return render(request, "core/ropa.html")

def poblar_bd(request):
    Producto.objects.all().delete()
    Producto.objects.create(id="0001", nombre='Dog Chow', descripcion="Bolsa 18kg, carne y pollo, adulto", precio='$20.600', descuento_sub='5%', descuento_oferta='10%', imagen="/images/dogChow18KG.jpg", categoria=Categoria.objects.get(idCategoria=1))
    Producto.objects.create(id="0002", nombre='Whiskas', descripcion="Bolsa de 500g, carne, adulto", precio='$10.500', descuento_sub='5%', descuento_oferta='5%', imagen="/images/whiskas_carne_500g.jpg", categoria=Categoria.objects.get(idCategoria=2))
    Producto.objects.create(id="0003", nombre='Huesitos', descripcion="Huesos sabor a pollo", precio='$15.000', descuento_sub='5%', descuento_oferta='17%', imagen="/images/huesitos_pollo.jpg", categoria=Categoria.objects.get(idCategoria=3))
    Producto.objects.create(id="0004", nombre='Master Dog', descripcion="Bolsa de 15kg, carne, adulto", precio='$19.000', descuento_sub='5%', descuento_oferta='22%', imagen="/images/Masterdog.jpg", categoria=Categoria.objects.get(idCategoria=1))
    Producto.objects.create(id="0005", nombre='Purina Cat Chow', descripcion="Bolsa 8kg, sabor pescado, adulto", precio='$13.500', descuento_sub='5%', descuento_oferta='30%', imagen="/images/purina_catchow_adultos_8kg.jpg", categoria=Categoria.objects.get(idCategoria=2))
    Producto.objects.create(id="0006", nombre='Pelotas perro', descripcion="Pelotas de goma para perros", precio='$6.500', descuento_sub='5%', descuento_oferta='8%', imagen="/images/pelota_perro.jpg", categoria=Categoria.objects.get(idCategoria=3))
    Producto.objects.create(id="0007", nombre='Cannes', descripcion="Bolsa 18kg, carne y cereales, adulto", precio='$25.000', descuento_sub='5%', descuento_oferta='15%', imagen="/images/cannes-carne-18.jpg", categoria=Categoria.objects.get(idCategoria=1))
    Producto.objects.create(id="0008", nombre='Don Kat', descripcion="Bolsa 1kg, pescado, cachorro", precio='$8.000', descuento_sub='5%', descuento_oferta='21%', imagen="/images/donkat_1kg_gaticos.jpg", categoria=Categoria.objects.get(idCategoria=2))
    return redirect(Producto, action='ins', id = '-1')