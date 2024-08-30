from django.contrib import admin
from .models import Pelicula, Genero, Sala, Funcion, Clasificacion, Asiento, Formato, Reserva, Usuario


# Register your models here.


class PeliculaAdmin(admin.ModelAdmin):
    list_display = ('Titulo', "Lanzamiento", "formato_duracion", "generos_list")

    def formato_duracion(self, obj):
        horas = obj.Duracion // 60
        minutos = obj.Duracion % 60
        return f"{horas}:{minutos:02d}h"

    formato_duracion.short_description = "Duracion"

    def generos_list(self, obj):
        return ", ".join(Genero.Genero for Genero in obj.Genero.all())

    generos_list.short_description = "Generos"


class GeneroAdmin(admin.ModelAdmin):
    list_display = ('Genero',)


class FormatoAdmin(admin.ModelAdmin):
    list_display = ('Tipo',)


class SalaAdmin(admin.ModelAdmin):
    list_display = ('Nombre', 'Formato')


class ClasificacionAdmin(admin.ModelAdmin):
    list_display = ('Clase'),


class FuncionAdmin(admin.ModelAdmin):
    list_display = ('IdFuncion', 'get_pelicula_titulo', 'get_sala_nombre', 'Horario', 'Precio')

    def get_pelicula_titulo(self, obj):
        return obj.IdPelicula.Titulo

    get_pelicula_titulo.short_description = 'Película'

    def get_sala_nombre(self, obj):
        return obj.IdSala.Nombre

    get_sala_nombre.short_description = 'Sala'


class AsientoAdmin(admin.ModelAdmin):
    list_display = ('formato_posicion', 'get_sala_nombre', 'Fila', 'Numero')

    def get_sala_nombre(self, obj):
        return obj.IdSala.Nombre

    get_sala_nombre.short_description = 'Sala'

    def formato_posicion(self, obj):
        fila = obj.Fila
        numero = obj.Numero
        return f"{fila}{numero}"

    formato_posicion.short_description = "Posicion"


class ReservaAdmin(admin.ModelAdmin):
    list_display = ('IdReserva', 'get_usuario_nombre', 'get_funcion_info', 'get_asientos_info', 'FechaReserva')
    list_filter = ('IdFuncion__IdPelicula__Titulo', 'FechaReserva')
    search_fields = ('IdUsuario__username', 'IdFuncion__IdPelicula__Titulo')

    def get_usuario_nombre(self, obj):
        return obj.IdUsuario.username
    get_usuario_nombre.short_description = 'Usuario'

    def get_funcion_info(self, obj):
        return f"{obj.IdFuncion.IdPelicula.Titulo} - {obj.IdFuncion.Horario}"
    get_funcion_info.short_description = 'Función'

    def get_asientos_info(self, obj):
        return ", ".join([f"{asiento.Fila}{asiento.Numero}" for asiento in obj.Asientos.all()])
    get_asientos_info.short_description = 'Asientos'


admin.site.register(Pelicula, PeliculaAdmin)
admin.site.register(Genero, GeneroAdmin)
admin.site.register(Sala, SalaAdmin)
admin.site.register(Funcion, FuncionAdmin)
admin.site.register(Clasificacion, ClasificacionAdmin)
admin.site.register(Asiento, AsientoAdmin)
admin.site.register(Formato, FormatoAdmin)
admin.site.register(Reserva, ReservaAdmin)
admin.site.register(Usuario)
