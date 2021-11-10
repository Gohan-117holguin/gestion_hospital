from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(Departamento)
class DepartamentosAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'tipo_departamento']
    search_fileds = ['nombre']
    list_filter = ['tipo_departamento']
    list_per_page = 10

@admin.register(Salas)
class SalasAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'tipo_sala']
    search_fileds = ['nombre']
    list_filter = ['tipo_sala']
    list_per_page = 10

@admin.register(Medicos)
class MedicosAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'especialidad']
    search_fileds = ['nombre']
    list_filter = ['especialidad']
    list_per_page = 10

@admin.register(Paciente)
class PacientesAdmin(admin.ModelAdmin):
    list_display = ['nombres', 'apellidos', 'tipo_paciente',]
    search_fileds = ['nombre']
    list_filter = ['tipo_paciente']
    list_per_page = 10