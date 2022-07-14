#  Authors: 
#  Franyelyn Rodríguez
#  Christopher Gedler <cgedler@gmail.com>
#  File name: views.py
#  Version: 1.0
#  Last Change: 29.06.2022 21:07:30 -04
#  Description: Modelos en Admin del Sistema Midipaaa

# Imports base para el sistema:
from django.contrib import admin
# Imports Modelos:
from .models import *


class CajaAdmin(admin.ModelAdmin):
   list_display = (
      'id',
      'descripcion',
      'articulos',
      'col_created',
      'col_created_by',
      'col_modified',
      'col_modified_by',
      'is_active'
   )
   search_fields = ['id']
   empty_value_display = '-empty-'
admin.site.register(Caja, CajaAdmin)


class CursoAdmin(admin.ModelAdmin):
   list_display = (
      'id',
      'descripcion',
      'col_created',
      'col_created_by',
      'col_modified',
      'col_modified_by',
      'is_active'
   )
   search_fields = ['id']
   empty_value_display = '-empty-'
admin.site.register(Curso, CursoAdmin)


class SectorAdmin(admin.ModelAdmin):
   list_display = (
      'id',
      'descripcion',
      'col_created',
      'col_created_by',
      'col_modified',
      'col_modified_by',
      'is_active'
   )
   search_fields = ['id']
   empty_value_display = '-empty-'
admin.site.register(Sector, SectorAdmin)


class BeneficiadoAdmin(admin.ModelAdmin):
   list_display = (
      'id_beneficiado',
      'sexo',
      'nacionalidad',
      'estado_civil',
      'primer_nombre',
      'segundo_nombre',
      'primer_apellido',
      'segundo_apellido',
      'fecha_nacimiento',
      'direccion',
      'celular',
      'telefono',
      'email',
      'sector',
      'familiares',
      'ingreso',
      'estudio',
      'vivienda',
      'tenencia',
      'col_created',
      'col_created_by',
      'col_modified',
      'col_modified_by',
      'is_active'
   )
   search_fields = ['id_beneficiado']
   empty_value_display = '-empty-'
admin.site.register(Beneficiado, BeneficiadoAdmin)


class CajaBeneficiadoAdmin(admin.ModelAdmin):
   list_display = (
      'id',
      'beneficiado',
      'caja')
   search_fields = ['beneficiado']
   empty_value_display = '-empty-'
admin.site.register(CajaBeneficiado, CajaBeneficiadoAdmin)


class CursoBeneficiadoAdmin(admin.ModelAdmin):
   list_display = (
      'id',
      'beneficiado',
      'curso')
   search_fields = ['beneficiado']
   empty_value_display = '-empty-'
admin.site.register(CursoBeneficiado, CursoBeneficiadoAdmin)
