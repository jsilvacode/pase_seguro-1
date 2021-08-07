from django.db import models
from django.core.files import File
from PIL import Image, ImageDraw
import qrcode
from io import BytesIO
from django.db.models.base import Model
from django.db.models.deletion import CASCADE



class AntecedentesPersonales(models.Model):
    rut = models.CharField(max_length=12, unique=True, verbose_name="RUT")
    nombres = models.CharField(max_length=200)
    apellidos = models.CharField(max_length=200)
    email = models.EmailField(max_length=100, verbose_name="correo electrónico")
    telefono = models.CharField(max_length=20, verbose_name="teléfono fijo / celular")
    
    def __str__(self):
        return self.rut

    class Meta:
        verbose_name = "Antecedente Personal"
        verbose_name_plural = "Antecedentes Personales"


class AntecedentesAcademicos(models.Model):
    facultad = models.CharField(max_length=100)
    carrera = models.CharField(max_length=100)

    def __str__(self):
        return '{} - {}'.format(self.facultad, self.carrera)

    class Meta:
        verbose_name = "Antecedente Académico"
        verbose_name_plural = "Antecedentes Académicos"


class ActividadAcademica(models.Model):
    fecha = models.DateField()
    hora_inicio = models.TimeField(verbose_name="horario de inicio")
    hora_fin = models.TimeField(verbose_name="horario de término")
    aula = models.CharField(max_length=100, verbose_name="aula / dependencia")
    asignatura = models.CharField(max_length=100)
    docente = models.CharField(max_length=200)
    facultad_carrera = models.ManyToManyField(
        AntecedentesAcademicos, related_name="get_faculty_career",
        verbose_name="facultad / carrera")

    class Meta:
        verbose_name = "Actividad Académica"
        verbose_name_plural = "Actividades Académicas"

    def __str__(self):
        return '{} - {}'.format(self.asignatura, self.docente)


class ActividadGeneral(models.Model):
    fecha = models.DateField()
    hora_inicio = models.TimeField(verbose_name="horario de inicio")
    hora_fin = models.TimeField(verbose_name="horario de término")
    dependencia = models.CharField(max_length=100, verbose_name="aula / dependencia")
    descripcion = models.TextField(verbose_name="descripción / comentario")

    def __str__(self):
        return "actividades generales"
    
    class Meta:
        verbose_name = "Actividad General"
        verbose_name_plural = "Actividades Generales"


class AntecedentesSanitarios(models.Model):
    # COVID-19
    CONTACTO_ESTRECHO_OPCIONES = (('sí', 'Sí'), ('no', 'No'))
    contacto_estrecho = models.CharField(
        max_length=10, choices=CONTACTO_ESTRECHO_OPCIONES, help_text="¿Ha tenido?."
    )

    # Antecedentes de salud I
    enfermedad_autoinmune = models.CharField(
        max_length=100, blank=True, verbose_name="enfermedad autoinmune"
    )
    enfermedad_cronica = models.CharField(
        max_length=100, blank=True, verbose_name="enfermedad crónica"
    )

    # Síntomas cardinales
    sintoma_fiebre = models.BooleanField(verbose_name="fiebre")
    sintoma_perdida_olfato = models.BooleanField(verbose_name="pérdida del olfato")
    sintoma_perdida_gusto = models.BooleanField(verbose_name="pérdida del gusto")

    # Síntomas no cardinales
    sintoma_tos = models.BooleanField(verbose_name="tos")
    sintoma_dolor_garganta = models.BooleanField(verbose_name="dolor de garganta")
    sintoma_secrecion_nasal = models.BooleanField(verbose_name="secreciones nasales")
    sintoma_respiratorio = models.BooleanField(verbose_name="dificultad respiratoria")
    sintoma_aumento_frecuencia = models.BooleanField(
        verbose_name="aumento de la frecuencia respiratoria"
    )
    sintoma_dolor_toracico = models.BooleanField(verbose_name="dolor torácico")
    sintoma_dolor_muscular = models.BooleanField(verbose_name="dolor muscular")
    sintoma_dolor_cabeza = models.BooleanField(verbose_name="dolor de cabeza")
    sintoma_fatiga = models.BooleanField(verbose_name="fatiga")
    sintoma_escalofrios = models.BooleanField(verbose_name="escalofríos")
    sintoma_diarrea = models.BooleanField(verbose_name="diarrea")
    sintoma_nausea_vomitos = models.BooleanField(verbose_name="náusea / vómitos")

    # Otros 
    sintoma_otro = models.CharField(max_length=200, blank=True, verbose_name="otros síntomas")

    # Antecedentes de salud II
    EMBARAZADA_OPCIONES = (('sí', 'Si'), ('no', 'No'))
    embarazo = models.CharField(
        max_length=10, blank=True, choices=EMBARAZADA_OPCIONES, help_text="¿Está?."
    )
    declaracion_confirmar = models.BooleanField(
        default=False, verbose_name="declaración de salud idónea", 
        help_text="Aceptar."
    )

    def __str__(self):
        return "antecedentes sanitarios"

    class Meta:
        verbose_name = "Antecedente Sanitario"
        verbose_name_plural = "Antecedentes Sanitarios"


class Estudiante(models.Model):
    antecedente_personal = models.ForeignKey(
        AntecedentesPersonales, on_delete=models.CASCADE, null=False, blank=False,
        verbose_name="antecedentes personales",
    )
    antecedente_academico = models.ForeignKey(
        AntecedentesAcademicos, on_delete=CASCADE, null=False, blank=False, 
        verbose_name="antecedentes académicos"),
    actividad_academica = models.ForeignKey(
        ActividadAcademica, on_delete=CASCADE, null=False, blank=False,
        verbose_name="actividades académicas", help_text="Eventos."
    )
    antecedente_sanitario = models.ForeignKey(
        AntecedentesSanitarios, on_delete=CASCADE, null=False, blank=False, 
        verbose_name="antecedentes sanitarios",
    )
    declaracion_archivo = models.FileField(
        upload_to='uploads/responsibilities/%Y/%m/%d/', blank=True, 
        verbose_name="declaración de responsabilidad", help_text="Doc adjunto."
    )

    def __str__(self):
        pass

    class Meta:
        verbose_name = "Estudiante"
        verbose_name_plural = "Estudiantes"


class Visita(models.Model):
    antecedente_personal = models.ForeignKey(
        AntecedentesPersonales, on_delete=models.CASCADE, null=False, blank=False,
        verbose_name="antecedentes personales",
    )
    antecedente_sanitario = models.ForeignKey(
        AntecedentesSanitarios, on_delete=CASCADE, null=False, blank=False, 
        verbose_name="antecedentes sanitarios",
    )
    actividad_general = models.ForeignKey(
        ActividadGeneral, on_delete=CASCADE, null=False, blank=False,
        verbose_name="actividades general", help_text="Eventos."
    )
    status_ingreso = models.BooleanField(default=True)
    qr_code = models.ImageField(upload_to="qr_codes", blank=True)

    def __str__(self):
        return str('visita')

    def save(self, *args, **kargs):
        qrcode_img = qrcode.make(self.antecedente_personal.rut)
        canvas = Image.new('RGB', (290, 290), "white")
        draw = ImageDraw.Draw(canvas)
        canvas.paste(qrcode_img)
        fname = f'qr_code-{self.antecedente_personal.rut}.pdf'
        buffer = BytesIO()
        canvas.save(buffer,'PDF')
        self.qr_code.save(fname, File(buffer), save=False)
        canvas.close()
        super().save(*args, **kargs)
    class Meta:
        verbose_name = 'Visita'
        verbose_name_plural = 'Visitas'