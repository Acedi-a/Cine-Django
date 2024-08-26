from django.contrib.auth import authenticate, logout, login
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.contrib import messages


from .models import Pelicula, Funcion  # Ajusta esto según tu modelo

def inicio(request):
    # Ordenar por fecha de creación en orden descendente y obtener los últimos 10 registros
    peliculas = Pelicula.objects.all().order_by('Lanzamiento')[:10]
    return render(request, r'cine/inicio.html', {'peliculas': peliculas})


def iniciov2(request):
    peliculas_destacadas = Pelicula.objects.order_by('-Lanzamiento')[:3]
    todas_peliculas = Pelicula.objects.all()

    context = {
        'peliculas_destacadas': peliculas_destacadas,
        'todas_peliculas': todas_peliculas,
    }

    return render(request, r'cine/iniciov2.html', context)


def detalle_pelicula(request, pelicula_id):
    pelicula = get_object_or_404(Pelicula, pk=pelicula_id)
    funciones = Funcion.objects.filter(IdPelicula=pelicula, Horario__gte=timezone.now()).order_by('Horario')

    # Agrupar funciones por fecha
    funciones_por_fecha = {}
    for funcion in funciones:
        fecha = funcion.Horario.date()
        if fecha not in funciones_por_fecha:
            funciones_por_fecha[fecha] = []
        funciones_por_fecha[fecha].append(funcion)

    context = {
        'pelicula': pelicula,
        'funciones_por_fecha': funciones_por_fecha,
    }
    return render(request, r'cine/detalle_pelicula.html', context)

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('iniciov2')
        else:
            messages.error(request, 'Usuario o contraseña incorrectos')
    return render(request, r'cine/login.html')

def logout_view(request):
    logout(request)
    return redirect('iniciov2')