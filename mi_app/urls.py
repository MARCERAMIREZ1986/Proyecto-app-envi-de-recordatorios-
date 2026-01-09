from django.urls import path
from . import views

urlpatterns = [ 
               path('prueba/',views.pagina_inicio, name="prueba"),
               path('nuevo_usuario/',views.nuevo_cliente,name='nuevo_usuario'),
               path('crear_usuario/',views.registrar_usuario,name='crear_usuario'),
                 path('cita/',views.crear_cita,name='cita'),
                  path('menu/',views.menu,name='menu'),
             
               ]