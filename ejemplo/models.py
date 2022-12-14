from django.db import models

class Familiar(models.Model):

    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=200)
    numero_pasaporte = models.IntegerField()
    fecha = models.DateField(default=True)

    def __str__(self):
      return f"{self.nombre}, {self.direccion}, {self.fecha}, {self.numero_pasaporte}, {self.id}"

class Dummy(models.Model):
    nombre = models.CharField(max_length=100)


class Auto(models.Model):

    marca = models.CharField(max_length=50)
    modelo = models.CharField(max_length=50)
    color = models.CharField(max_length=10)
    patente = models.CharField(max_length=10)

    def __str__(self):
      return f"{self.marca}, {self.modelo}, {self.color}, {self.patente}, {self.id}"


class Mascota(models.Model):

    nombre = models.CharField(max_length=50)
    animal = models.CharField(max_length=50)
    raza = models.CharField(max_length=50)
    fecha = models.DateField(default=True)

    def __str__(self):
      return f"{self.nombre}, {self.animal}, {self.raza}, {self.fecha}, {self.id}"
