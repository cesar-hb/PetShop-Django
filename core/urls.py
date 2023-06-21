from django.urls import path
from .views import home, poblar_bd, producto, producto_tienda, producto_ficha


urlpatterns = [
    path('', home, name="home"),
    path('poblar_bd', poblar_bd, name="poblar_bd"),
    path('producto/<action>/<id>', producto, name="producto"),
    path('producto_tienda', producto_tienda, name="producto_tienda"),
    path('producto_ficha/<id>', producto_ficha, name="producto_ficha"),
]
