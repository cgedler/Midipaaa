#  Authors: 
#  Franyelyn Rodríguez
#  Christopher Gedler <cgedler@gmail.com>
#  File name: views.py
#  Version: 1.0
#  Last Change: 29.06.2022 21:07:30 -04
#  Description: Formularios del Sistema Midipaaa

# Imports base para el sistema:
from django import forms
from django.forms import ModelForm
from django.forms import Textarea, CharField, TextInput, ChoiceField
from django.forms import Select, NumberInput, DateField, DateTimeInput
# Imports Modelos:
from .models import *


class DateInput(forms.DateInput):
    input_type = 'date'


class BeneficiadoForm(forms.ModelForm):
    class Meta:
        model = Beneficiado
        fields = [
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
        'tenencia']
        widgets = {
            'fecha_nacimiento': DateInput()
        }

    def __init__(self, *args, **kwargs):
        super(BeneficiadoForm, self).__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })


class AsignarCajaForm(forms.ModelForm):
    class Meta:
        model = CajaBeneficiado
        fields = [
        'beneficiado',
        'caja']

    def __init__(self, *args, **kwargs):
        super(AsignarCajaForm, self).__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })


class AsignarCursoForm(forms.ModelForm):
    class Meta:
        model = CursoBeneficiado
        fields = [
        'beneficiado',
        'curso']

    def __init__(self, *args, **kwargs):
        super(AsignarCursoForm, self).__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })


class CajaForm(forms.ModelForm):
    class Meta:
        model = Caja
        fields = [
        'id',
        'descripcion',
        'articulos']

    def __init__(self, *args, **kwargs):
        super(CajaForm, self).__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })


class CursoForm(forms.ModelForm):
    class Meta:
        model = Curso
        fields = [
        'id',
        'descripcion']

    def __init__(self, *args, **kwargs):
        super(CursoForm, self).__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })


class SectorForm(forms.ModelForm):
    class Meta:
        model = Sector
        fields = [
        'id',
        'descripcion']

    def __init__(self, *args, **kwargs):
        super(SectorForm, self).__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })
