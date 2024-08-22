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
    Lanzamiento = models.DateField()
    Clasificacion = models.ForeignKey(Clasificacion, on_delete=models.CASCADE)
    Duracion = models.IntegerField()
    Genero = models.ManyToManyField(Genero)
    Portada = models.ImageField(upload_to='cine/media/')
    Trailer = models.CharField(max_length=200)
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
    def __str__(self):
        return f"{self.IdAsiento}"

class Reserva(models.Model):
    IdReserva = models.AutoField(primary_key=True)
    IdAsiento = models.ForeignKey(Asiento, on_delete= models.CASCADE)
    IdUsuario = models.ForeignKey(Usuario, on_delete= models.CASCADE)
    IdFuncion = models.ForeignKey(Funcion, on_delete= models.CASCADE)
    FechaReserva = models.DateTimeField(auto_now_add=True)
    class Meta:
        unique_together = ('IdFuncion', 'IdAsiento')  # Asegura que un asiento no pueda ser reservado dos veces para la misma función
        
    def __str__(self): 
        return f"self.IdReserva"


    