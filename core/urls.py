from django.urls import path
from .views import home,nosotros, poblar_bd, producto, producto_tienda, producto_ficha,datos_usuario
from .views import iniciar_sesion, registrar_usuario, cerrar_sesion, ropa,administrar,admin_users,admin_bodega


urlpatterns = [
    path('', home, name="home"),
    path('poblar_bd', poblar_bd, name="poblar_bd"),
    path('producto/<action>/<id>', producto, name="producto"),
    path('nosotros/', nosotros, name="nosotros"),
    path('administrar/', administrar, name="administrar"),
    path('admin_users/', admin_users, name="admin_users"),
    path('producto_tienda', producto_tienda, name="producto_tienda"),
    path('producto_ficha/<id>', producto_ficha, name="producto_ficha"),
    path('iniciar_sesion/', iniciar_sesion, name="iniciar_sesion"),
    path('cerrar_sesion/', cerrar_sesion, name='cerrar_sesion'),
    path('registrar_usuario/', registrar_usuario.as_view(), name="registrar_usuario"),
    path('datos_usuario/', datos_usuario, name="datos_usuario"),
    path('ropa/', ropa, name="ropa"),
    path('admin_bodega/', admin_bodega, name="admin_bodega"),
]
