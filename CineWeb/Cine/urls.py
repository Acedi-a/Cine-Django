from django.urls import path
from . import views
from .views import detalles_view

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('detalles/', detalles_view, name='detalles')
]