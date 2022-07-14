#  Authors: 
#  Franyelyn Rodríguez
#  Christopher Gedler <cgedler@gmail.com>
#  File name: views.py
#  Version: 1.0
#  Last Change: 29.06.2022 21:07:30 -04
#  Description: Modelos del Sistema Midipaaa

# Imports base para el sistema:
from django.db import models
from crum import get_current_user
from django.utils import timezone
from django.utils.html import format_html


class Base(models.Model):
    """ Description: Base para las demás tablas """
    # Attributes:
    created = models.DateTimeField(
        auto_now_add = True,
        verbose_name = u'Created')
    created_by = models.ForeignKey(
        'auth.User',
        null = True,
        blank = True,
        default = None,
        on_delete = models.DO_NOTHING,
        related_name = '%(app_label)s_%(class)s_created_by',
        verbose_name = u'Create by',
        db_column = 'create_by')
    modified = models.DateTimeField(
        null = True,
        blank = True,
        verbose_name = u'Modified')
    modified_by = models.ForeignKey(
        'auth.User',
        null = True,
        blank = True,
        default = None,
        on_delete = models.DO_NOTHING,
        related_name = '%(app_label)s_%(class)s_modified_by',
        verbose_name = u'Modified by',
        db_column = 'modified_by')
    is_active = models.BooleanField(
        null = True,
        blank = True,
        default = True,
        verbose_name = u'is_active')

    # Methods:
    def col_created(self):
        return format_html('<span style = "color: #0091EA;">{0}</span>', self.created)
    col_created.short_description = 'Created'

    def col_created_by(self):
        return format_html('<span style = "color: #558B2F;">{0}</span>', self.created_by)
    col_created_by.short_description = 'Created by'

    def col_modified(self):
        return format_html('<span style = "color: #0091EA;">{0}</span>', self.modified)
    col_modified.short_description = 'Modified'

    def col_modified_by(self):
        return format_html('<span style = "color: #F57C00;">{0}</span>', self.modified_by)
    col_modified_by.short_description = 'Modified by'

    class Meta:
        abstract = True


class Caja(Base):
    """ Description: Modelo de la clase Caja Alimentaria"""
    # Attributes:
    descripcion = models.CharField(
        max_length = 250,
        null = True,
        blank = True,
        default = u'',
        help_text = u'Descripción de la caja',
        verbose_name = u'Descripcion',
        db_column = 'descripcion')
    articulos = models.CharField(
        max_length = 255,
        null = True,
        blank = True,
        default = u'',
        help_text = u'Listado de Articulos',
        verbose_name = u'Articulos',
        db_column = 'articulos')

    # Methods:
    def __str__(self):
        cadena = '{0} - {1}'
        return cadena.format(self.id, self.descripcion)

    def save(self, *args, **kwargs):
        user = get_current_user()
        if user and not user.pk:
            user = None
        if not self.pk:
            self.created_by = user
        self.modified_by = user
        self.modified = timezone.now()
        return super(Caja, self).save(*args, **kwargs)

    class Meta:
        db_table = 'caja_alimentaria'
        ordering = ['descripcion']
        verbose_name = 'caja'
        verbose_name_plural = 'cajas'


class Curso(Base):
    """ Description: Modelo de los Cursos"""
    # Attributes:
    descripcion = models.CharField(
        max_length = 250,
        null = True,
        blank = True,
        default = u'',
        help_text = u'Descripción de la caja',
        verbose_name = u'Descripcion',
        db_column = 'descripcion')

    # Methods:
    def __str__(self):
        cadena = '{0} - {1}'
        return cadena.format(self.id, self.descripcion)

    def save(self, *args, **kwargs):
        user = get_current_user()
        if user and not user.pk:
            user = None
        if not self.pk:
            self.created_by = user
        self.modified_by = user
        self.modified = timezone.now()
        return super(Curso, self).save(*args, **kwargs)

    class Meta:
        db_table = 'curso'
        ordering = ['descripcion']
        verbose_name = 'curso'
        verbose_name_plural = 'cursos'


class Sector(Base):
    """ Description: Modelo de los Sectores"""
    # Attributes:
    descripcion = models.CharField(
        max_length = 250,
        null = True,
        blank = True,
        default = u'',
        help_text = u'Descripción del Sector',
        verbose_name = u'Descripcion',
        db_column = 'descripcion')

    # Methods:
    def __str__(self):
        cadena = '{0} - {1}'
        return cadena.format(self.id, self.descripcion)

    def save(self, *args, **kwargs):
        user = get_current_user()
        if user and not user.pk:
            user = None
        if not self.pk:
            self.created_by = user
        self.modified_by = user
        self.modified = timezone.now()
        return super(Sector, self).save(*args, **kwargs)

    class Meta:
        db_table = 'sector'
        ordering = ['descripcion']
        verbose_name = 'sector'
        verbose_name_plural = 'sectores'


class Beneficiado(Base):
    """ Description: Modelo de la clase Beneficiado"""
    # Constant:
    SEX_CHOICES = [
        ('1','Masculino'),
        ('2','Femenino')
    ]
    NAC_CHOICES = [
        ('V','Venezolano(a)'),
        ('E','Extranjero(a)')
    ]
    CIVIL_CHOICES = [
        ('S','Soltero(a)'),
        ('C','Casado(a)'),
        ('D','Divorciado(a)'),
        ('V','Viudo(a)')
    ]
    INGRESO_CHOICES = [
        ('1','Menor al Sueldo Minimo'),
        ('2','Sueldo Minimo'),
        ('3','Mayor al Sueldo Minimo'),
        ('4','Otro')
    ]
    ESTUDIO_CHOICES = [
        ('1','Primaria'),
        ('2','Secundaria'),
        ('3','Técnica'),
        ('4','Superior'),
        ('5','Otro')
    ]
    VIVIENDA_CHOICES = [
        ('1','Apartamento'),
        ('2','Casa'),
        ('3','Quinta'),
        ('4','Otro')
    ]
    TENENCIA_CHOICES = [
        ('1','Propia'),
        ('2','Alquilada'),
        ('3','Compartida con Familiares'),
        ('4','Otro')
    ]

    # Attributes:
    # Personales:
    id_beneficiado = models.IntegerField(
        primary_key = True,
        verbose_name = u'Cédula del Beneficiado',
        help_text = u'Por favor ingrese solo el número')
    sexo = models.CharField(
        max_length = 1,
        choices = SEX_CHOICES,
        verbose_name = u'Sexo',
        help_text = u'Por favor seleccione el sexo')
    nacionalidad = models.CharField(
        max_length = 1,
        choices = NAC_CHOICES,
        verbose_name = u'Nacionalidad',
        help_text = u'Por favor seleccione la Nacionalidad')
    estado_civil = models.CharField(
        max_length = 1,
        choices = CIVIL_CHOICES,
        verbose_name = u'Estado Civil',
        help_text = u'Por favor seleccione el estado civil')
    primer_nombre = models.CharField(
        max_length = 60,
        null = False,
        help_text = u'Por favor ingrese el primer nombre',
        verbose_name = u'Primer Nombre')
    segundo_nombre = models.CharField(
        max_length = 60,
        null = True,
        blank = True,
        help_text = u'Por favor ingrese el segundo nombre',
        verbose_name = u'Segundo Nombre')
    primer_apellido = models.CharField(
        max_length = 60,
        null = False,
        help_text = u'Por favor ingrese el primer apellido',
        verbose_name = u'Primer Apellido') 
    segundo_apellido = models.CharField(
        max_length = 60,
        null = True,
        blank = True,
        help_text = u'Por favor ingrese el segundo apellido',
        verbose_name = u'Segundo Apellido')
    fecha_nacimiento = models.DateField(
        null = True,
        blank = True,
        verbose_name = u'Fecha de Nacimiento')
    # Contacto:
    direccion = models.TextField(
        max_length = 254,
        null = True,
        blank = True,
        verbose_name = u'Dirección')
    celular = models.CharField(
        max_length = 16,
        null = True,
        blank = True,
        default = '(0424)-000-00-00',
        verbose_name = u'Celular',
        help_text = u'Por favor ingrese el celular parecido al ejemplo')
    telefono = models.CharField(
        max_length = 16,
        null = True,
        blank = True,
        default = '(0212)-000-00-00',
        verbose_name = u'Teléfono',
        help_text = u'Por favor ingrese el teléfono parecido al ejemplo')
    email = models.EmailField(
        max_length = 254,
        null = True,
        blank = True,
        default = 'empleado@email.com',
        verbose_name = u'Email',
        help_text = u'Por favor ingrese el email parecido al ejemplo')
    sector = models.ForeignKey(
        Sector,
        null = True,
        blank = True,
        on_delete = models.CASCADE)
    # Familiares:
    familiares = models.PositiveIntegerField(
        null = True,
        blank = True,
        verbose_name = u'Cantidad de Familiares')
    # socio-económicos
    ingreso = models.CharField(
        max_length = 1,
        choices = INGRESO_CHOICES,
        verbose_name = u'Ingreso',
        help_text = u'Por favor seleccione el nivel de ingreso')
    estudio = models.CharField(
        max_length = 1,
        choices = ESTUDIO_CHOICES,
        verbose_name = u'Estudio',
        help_text = u'Por favor seleccione el nivel de estudio')
    vivienda = models.CharField(
        max_length = 1,
        choices = VIVIENDA_CHOICES,
        verbose_name = u'Vivienda',
        help_text = u'Por favor seleccione el tipo de vivienda')
    tenencia = models.CharField(
        max_length = 1,
        choices = TENENCIA_CHOICES,
        verbose_name = u'Tenencia',
        help_text = u'Por favor seleccione la tenencia de la vivienda')

    # Methods:
    def __str__(self):
        cadena = '{0} - {1} {2}'
        return cadena.format(
            self.id_beneficiado,
            self.primer_apellido,
            self.primer_nombre)

    def save(self, *args, **kwargs):
        user = get_current_user()
        if user and not user.pk:
            user = None
        if not self.pk:
            self.created_by = user
        self.modified_by = user
        self.modified = timezone.now()
        return super(Beneficiado, self).save(*args, **kwargs)

    class Meta:
        db_table = 'beneficiado'
        ordering = ['id_beneficiado']
        verbose_name = 'beneficiado'
        verbose_name_plural = 'beneficiados'


class CajaBeneficiado(Base):
    """ Description: Modelo de la clase CajaBeneficiado"""
    # Attributes:
    beneficiado = models.OneToOneField(
        Beneficiado,
        verbose_name = u'Cédula del Beneficiado',
        on_delete = models.CASCADE)
    caja = models.ForeignKey(
        Caja,
        verbose_name = u'Modelo de Caja',
        on_delete = models.CASCADE)

    # Methods:
    def __str__(self):
        cadena = '{0} - {1} {2}'
        return cadena.format(
            self.beneficiado,
            self.caja)

    def save(self, *args, **kwargs):
        user = get_current_user()
        if user and not user.pk:
            user = None
        if not self.pk:
            self.created_by = user
        self.modified_by = user
        self.modified = timezone.now()
        return super(CajaBeneficiado, self).save(*args, **kwargs)

    class Meta:
        db_table = 'caja_beneficiado'
        ordering = ['beneficiado']
        verbose_name = 'CajaBeneficiado'
        verbose_name_plural = 'CajaBeneficiados'


class CursoBeneficiado(Base):
    """ Description: Modelo de la clase CajaBeneficiado"""
    # Attributes:
    beneficiado = models.OneToOneField(
        Beneficiado,
        verbose_name = u'Cédula del Beneficiado',
        on_delete = models.CASCADE)
    curso = models.ForeignKey(
        Curso,
        verbose_name = u'Curso',
        on_delete = models.CASCADE)

    # Methods:
    def __str__(self):
        cadena = '{0} - {1} {2}'
        return cadena.format(
            self.beneficiado,
            self.curso)

    def save(self, *args, **kwargs):
        user = get_current_user()
        if user and not user.pk:
            user = None
        if not self.pk:
            self.created_by = user
        self.modified_by = user
        self.modified = timezone.now()
        return super(CursoBeneficiado, self).save(*args, **kwargs)

    class Meta:
        db_table = 'curso_beneficiado'
        ordering = ['beneficiado']
        verbose_name = 'CursoBeneficiado'
        verbose_name_plural = 'CursoBeneficiados'


class HistoricoEntrega(Base):
    """ Description: Modelo de la clase Historico Entrega de cajas"""
    # Attributes:
    beneficiado = models.CharField(
        max_length = 255,
        null = False,
        blank = False,
        verbose_name = u'Beneficiado')
    caja = models.CharField(
        max_length = 255,
        null = False,
        blank = False,
        verbose_name = u'Modelo de Caja')

    # Methods:
    def __str__(self):
        cadena = '{0} - {1} {2}'
        return cadena.format(
            self.beneficiado,
            self.caja)

    def save(self, *args, **kwargs):
        user = get_current_user()
        if user and not user.pk:
            user = None
        if not self.pk:
            self.created_by = user
        self.modified_by = user
        self.modified = timezone.now()
        return super(HistoricoEntrega, self).save(*args, **kwargs)

    class Meta:
        db_table = 'historico_entrega'
        ordering = ['created']
        verbose_name = 'HistoricoEntrega'
        verbose_name_plural = 'HistoricoEntregas'
