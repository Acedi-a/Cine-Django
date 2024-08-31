from django.db import models
from django.contrib.auth.models import User



# Create your models here.

class Usuario(models.Model):
    Nombre = models.CharField(max_length=100)
    Apellido = models.CharField(max_length=100)
    CI = models.IntegerField(unique=True)
    Rol = models.BooleanField(default=False)
    FechaRegistro= models.DateField()
    Estado = models.BooleanField(default=True)
    def __str__(self):
        return f"{self.Nombre} {self.Apellido} (CI: {self.CI})"
    
class Genero(models.Model):
    IdGenero = models.AutoField(primary_key=True)
    Genero = models.CharField(max_length=100)
    def __str__(self):
        return self.Genero
    
class Clasificacion(models.Model):
    IdGenero = models.AutoField(primary_key=True)
    Clase = models.CharField(max_length=100)
    def __str__(self):
        return self.Clase

class Pelicula(models.Model):
    Titulo = models.CharField(max_length=100)
    Descripcion = models.TextField(default="Pelicula")
    Lanzamiento = models.DateField()
    Clasificacion = models.ForeignKey(Clasificacion, on_delete=models.CASCADE)
    Duracion = models.IntegerField()
    Genero = models.ManyToManyField(Genero)
    Portada = models.ImageField(upload_to='cine/media/')
    Trailer = models.CharField(max_length=400)
    def __str__(self):
        return f"Titulo: {self.Titulo}"

class Formato(models.Model):
    IdFormato = models.AutoField(primary_key=True)
    Tipo = models.CharField(max_length=40)
    def __str__(self):
        return self.Tipo
    

class Sala(models.Model):
    IdSala = models.AutoField(primary_key=True)
    Nombre = models.CharField(max_length=100)
    Formato = models.ForeignKey(Formato, on_delete=models.CASCADE)
    Estado = models.BooleanField(default=True)
    def __str__(self):
        return self.Nombre

class Funcion(models.Model):
    IdFuncion = models.AutoField(primary_key=True)
    IdPelicula = models.ForeignKey(Pelicula, on_delete=models.CASCADE)
    IdSala = models.ForeignKey(Sala, on_delete=models.CASCADE)
    Horario = models.DateTimeField()
    Precio = models.PositiveIntegerField()
    def __str__(self):
        return f"Función {self.IdFuncion}"
    
class Asiento(models.Model):
    IdAsiento = models.AutoField(primary_key=True)
    IdSala = models.ForeignKey(Sala, on_delete=models.CASCADE)
    Numero = models.PositiveIntegerField()
    Fila = models.CharField(max_length=3)
    Estado = models.BooleanField(default=True)
    def __str__(self):
        return f"{self.IdAsiento}"


class Reserva(models.Model):
    IdReserva = models.AutoField(primary_key=True)
    IdUsuario = models.ForeignKey(User, on_delete=models.CASCADE)
    IdFuncion = models.ForeignKey(Funcion, on_delete=models.CASCADE)
    Asientos = models.ManyToManyField(Asiento)
    FechaReserva = models.DateTimeField(auto_now_add=True)
    ReservaQR = models.ImageField(upload_to='cine/media/reservaQR/')

    def __str__(self):
        return f"Reserva {self.IdReserva} - {self.IdUsuario.username}"

    @staticmethod
    def asientos_reservados(funcion_id):
        return Asiento.objects.filter(reserva__IdFuncion_id=funcion_id).values_list('pk', flat=True)


    