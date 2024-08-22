from django.shortcuts import render
from .models import Pelicula  # Ajusta esto según tu modelo

def inicio(request):
    # Ordenar por fecha de creación en orden descendente y obtener los últimos 10 registros
    peliculas = Pelicula.objects.all().order_by('Lanzamiento')[:10]
    return render(request, r'cine/inicio.html', {'peliculas': peliculas})
def detalles_view(request):
    return render(request, 'DetallesPeli.html')