from django.shortcuts import redirect, render
from .models import Producto, Categoria
from .forms import ProductoForm


# Create your views here.


def home(request):
    return render(request, "templates\core/home.html")


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

def poblar_bd(request):
    Producto.objects.all().delete()
    Producto.objects.create(id="0001", nombre='Dog Chow', descripcion="Dog Chow adulto", precio='$10.000', descuento_sub='5%', descuento_oferta='10%', imagen="images/dogChow18KG", categoria=Categoria.objects.get(idCategoria=1))
    Producto.objects.create(id="0002", nombre='Dog Chow', descripcion="Dog Chow adulto", precio='$13.500', descuento_sub='5%', descuento_oferta='5%', imagen="images/dogChow18KG", categoria=Categoria.objects.get(idCategoria=2))
    Producto.objects.create(id="0003", nombre='Dog Chow', descripcion="Dog Chow adulto", precio='$15.000', descuento_sub='5%', descuento_oferta='17%', imagen="images/dogChow18KG", categoria=Categoria.objects.get(idCategoria=3))
    Producto.objects.create(id="0004", nombre='Dog Chow', descripcion="Dog Chow adulto", precio='$9.000', descuento_sub='5%', descuento_oferta='22%', imagen="images/dogChow18KG", categoria=Categoria.objects.get(idCategoria=1))
    Producto.objects.create(id="0005", nombre='Dog Chow', descripcion="Dog Chow adulto", precio='$8.500', descuento_sub='5%', descuento_oferta='30%', imagen="images/dogChow18KG", categoria=Categoria.objects.get(idCategoria=2))
    Producto.objects.create(id="0006", nombre='Dog Chow', descripcion="Dog Chow adulto", precio='$15.500', descuento_sub='5%', descuento_oferta='8%', imagen="images/dogChow18KG", categoria=Categoria.objects.get(idCategoria=3))
    Producto.objects.create(id="0007", nombre='Dog Chow', descripcion="Dog Chow adulto", precio='$12.000', descuento_sub='5%', descuento_oferta='15%', imagen="images/dogChow18KG", categoria=Categoria.objects.get(idCategoria=1))
    Producto.objects.create(id="0008", nombre='Dog Chow', descripcion="Dog Chow adulto", precio='$8.000', descuento_sub='5%', descuento_oferta='21%', imagen="images/dogChow18KG", categoria=Categoria.objects.get(idCategoria=2))
    
    return redirect(Producto, action='ins', id = '-1')