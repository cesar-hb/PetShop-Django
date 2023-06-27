from django.urls import path
from .views import home, poblar_bd, producto, producto_tienda, producto_ficha
from .views import iniciar_sesion, registrar_usuario, cerrar_sesion


urlpatterns = [
    path('', home, name="home"),
    path('poblar_bd', poblar_bd, name="poblar_bd"),
    path('producto/<action>/<id>', producto, name="producto"),
    path('producto_tienda', producto_tienda, name="producto_tienda"),
    path('producto_ficha/<id>', producto_ficha, name="producto_ficha"),
    path('iniciar_sesion/', iniciar_sesion, name="iniciar_sesion"),
    path('cerrar_sesion/', cerrar_sesion, name='cerrar_sesion'),
    path('registrar_usuario/', registrar_usuario.as_view(), name="registrar_usuario")
]
