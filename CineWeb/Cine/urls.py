from django.urls import path
from . import views

urlpatterns = [
    path('', views.iniciov2, name='iniciov2'),
    path('pelicula/<int:pelicula_id>/', views.detalle_pelicula, name='detalle_pelicula'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('funcion/<int:funcion_id>/seleccion-asientos/', views.seleccion_asientos, name='seleccion_asientos'),
    path('reservar-asientos/', views.reservar_asientos, name='reservar_asientos'),
    path('registro/', views.registro_usuario, name='registro_usuario'),
    path('editar-perfil/', views.editar_perfil, name='editar_perfil'),
    path('reservas_usuario/', views.reservas_usuario, name='reservas_usuario'),

]