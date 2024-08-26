from django.urls import path
from . import views

urlpatterns = [
    path('', views.iniciov2, name='iniciov2'),
    path('pelicula/<int:pelicula_id>/', views.detalle_pelicula, name='detalle_pelicula'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),

]