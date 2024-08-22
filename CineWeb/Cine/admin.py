from django.contrib import admin
from .models import Pelicula, Genero

# Register your models here.



class PeliculaAdmin(admin.ModelAdmin):
    list_display = ('Titulo',"Lanzamiento","formato_duracion", "generos_list")
    
    def formato_duracion(self,obj):
        horas = obj.Duracion // 60
        minutos = obj.Duracion % 60
        return f"{horas}:{minutos:02d}h"
    formato_duracion.short_description = "Duracion"
    
    def generos_list(self, obj):
        return ", ".join(Genero.Nombre for Genero in obj.Genero.all()) 
    generos_list.short_description = "Generos"
class GeneroAdmin(admin.ModelAdmin):
    list_display = ('Nombre',)

admin.site.register(Pelicula, PeliculaAdmin)
admin.site.register(Genero)