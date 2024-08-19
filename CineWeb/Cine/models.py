from django.db import models

# Create your models here.

class Usuario(models.Model):
    Nombre = models.CharField(max_length=100)
    Apellido = models.CharField(max_length=100)
    CI = models.IntegerField(unique=True)
    Rol = models.BooleanField(default=False)
    FechaRegistro= models.DateField()
    Estado = models.BooleanField(default=True)
    def __str__(self):
        return self.Nombre, self.CI, self.Rol
    
class Genero(models.Model):
    IdGenero = models.AutoField(primary_key=True)
    Nombre = models.CharField(max_length=100)
    def __str__(self):
        return self.Nombre
    
class Pelicula(models.Model):
    Nombre = models.CharField(max_length=100)
    Lanzamiento = models.DateField()
    Clasificacion = models.CharField(max_length=100)
    Duracion = models.IntegerField()
    Genero = models.ManyToManyField(Genero)
    def __str__(self):
        return self.Nombre

class Sala(models.Model):
    IdSala = models.AutoField(primary_key=True)
    Nombre = models.CharField(max_length=100)
    Formato = models.BooleanField(default=False)
    Estado = models.BooleanField(default=True)
    def __str__(self):
        return self.IdSala

class Funcion(models.Model):
    IdFuncion = models.AutoField(primary_key=True)
    IdPelicula = models.ForeignKey(Pelicula, on_delete=models.CASCADE)
    IdSala = models.ForeignKey(Sala, on_delete=models.CASCADE)
    Horario = models.DateTimeField()
    Precio = models.PositiveIntegerField()
    def __str__(self):
        return self.IdFuncion
    
class Asiento(models.Model):
    IdAsiento = models.AutoField(primary_key=True)
    IdSala = models.ForeignKey(Sala, on_delete=models.CASCADE)
    Numero = models.PositiveIntegerField()
    Fila = models.CharField(max_length=3)
    def __str__(self):
        return self.IdAsiento, self.Fila

class Reserva(models.Model):
    IdReserva = models.AutoField(primary_key=True)
    IdAsiento = models.ForeignKey(Asiento, on_delete= models.CASCADE)
    IdUsuario = models.ForeignKey(Usuario, on_delete= models.CASCADE)
    def __str__(self): 
        return self.IdReserva


    