from django.db import models
from django.db.models.fields.related import ForeignKey

# Create your models here.
class Departamento(models.Model):
    nombre = models.CharField(max_length=50)
    tipo_departamento = models.CharField(max_length=50)
    direccion = models.TextField()
    
    def __str__(self):
        return self.nombre

opciones_salas = [
    [0, 'Privada'],
    [1, 'Publica'],
    [2, 'Especial']
]

class Salas(models.Model):
    nombre = models.CharField(max_length=50)
    tipo_sala = models.IntegerField(choices=opciones_salas)
    cant_pacientes = models.IntegerField()
    departamento = models.ForeignKey(Departamento, on_delete=models.PROTECT)
    
    def __str__(self):
        return self.nombre

class Medicos(models.Model):
    nombre = models.CharField(max_length=50)
    especialidad = models.CharField(max_length=50)
    tipo_sangre = models.CharField(max_length=5)
    edad = models.IntegerField()
    departamento = models.ForeignKey(Departamento, on_delete=models.PROTECT)
    
    def __str__(self):
        return self.nombre

opciones_paciente = [
    [0, 'Nuevo'],
    [1, 'Habitual']
]

opciones_tipodoc = [
    [0, 'CC'],
    [1, 'TI'],
    [2, 'RC'],
    [3, 'Otro']
]

class Paciente(models.Model):
    nombres = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=50)
    tipo_sangre = models.CharField(max_length=5)
    descripcion = models.TextField()
    tipo_doc = models.IntegerField(choices=opciones_tipodoc)
    antecedentes = models.TextField()
    tipo_paciente = models.IntegerField(choices=opciones_paciente)
    
    def __str__(self):
        return self.nombre