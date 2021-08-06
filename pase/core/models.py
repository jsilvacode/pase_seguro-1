from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields.related import ForeignKey


class ActividadAcademica(models.Model):
    fecha = models.DateField()
    hora_inicio = models.DateField()
    hora_fin = models.DateField()
    aula = models.CharField()
    asignatura = models.CharField()
    docente = models.CharField()
    facultad = models.CharField()
    carrera = models.CharField()

    class Meta:
        verbose_name = 'Actividad Academica'
        verbose_name_plural = 'Actividades Académicas'

    def __str__(self):
        return '{} - {}'.format(self.asignatura, self.docente)


class ActividadGeneral(models.Model):
    fecha = models.DateField()
    hora_inicio = models.DateField()
    hora_fin = models.DateField()
    dependencia = models.CharField()
    descripcion = models.TextField()

    def __str__(self):
        pass

    class Meta:
        verbose_name = 'Actividad General'
        verbose_name_plural = 'Actividades Generales'


class AntecedenteAcademico(models.Model):
    facultad = models.CharField()
    carrera = models.CharField()

    def __str__(self):
        return '{} - {}'.format(self.facultad, self.carrera)

    class Meta:
        verbose_name = 'Antecedente Académico'
        verbose_name_plural = 'Antecedentes Académicos'


class AntecedentesPersonales(models.Model):
    rut = models.CharField()
    nombres = models.CharField()
    apellidos = models.CharField()
    email = models.EmailField()
    telefono = models.CharField()
    
    def __str__(self):
        return self.rut

    class Meta:
        verbose_name = 'Antecedente Sanitario'
        verbose_name_plural = 'Antecedentes Sanitarios'


class AntecedenteSanitario(models.Model):
    contacto_estrecho = models.BooleanField()
    sintomas_cardinales = models.BooleanField()
    sintomas_no_cardinales = models.BooleanField()
    declaracion_salud = models.FileField()

    def __str__(self):
        pass

    class Meta:
        verbose_name = 'Antecedente Sanitario'
        verbose_name_plural = 'Antecedentes Sanitarios'


class Estudiante(models.Model):
    antecedente_personal = models.ForeignKey(
        'AntecedentesPersonales', verbose_name='antecedentes personales',
        null=False, blank=False, on_delete=models.CASCADE)
    antecedente_academico = models.ForeignKey(
        'AntecedenteAcademico', on_delete=CASCADE,
        null=False, blank=False, verbose_name='Antecedente Academico'
    )
    actividad_academica = models.ForeignKey(
        'ActividadAcademica', verbose_name='Actividad Academica',
        null=False, blank=False, on_delete=CASCADE
    )
    antecedente_sanitario = models.ForeignKey(
        'AntecedenteSanitario', verbose_name='Antecedente Sanitario',
        null=False, blank=False, on_delete=CASCADE
    )
    declaracion_salud = models.FileField()

    def __str__(self):
        pass

    class Meta:
        verbose_name = 'Estudiante'
        verbose_name_plural = 'Estudiantes'