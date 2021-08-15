from django import forms
from .models import (AntecedentesPersonales, AntecedentesAcademicos, Register_in_out,
                     AntecedentesSanitarios, ActividadGeneral, ActividadAcademica, Carrera)


class PerfilForm(forms.ModelForm):
    class Meta:
        model = AntecedentesPersonales
        fields = ['rut', 
                  'nombre',
                  'apellido',
                  'email',
                  'telefono']
        widgets = {
            'rut': forms.TextInput(attrs={'class': 'form-control'}),
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'apellido': forms.TextInput(attrs={'class': 'form-control',}),
            'email': forms.TextInput(attrs={'class': 'form-control'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control'}),
        }


class EducacionForm(forms.ModelForm):
    class Meta:
        model = AntecedentesAcademicos
        fields = ['facultad', 'carrera']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['carrera'].queryset = Carrera.objects.all()


class DeclaracionForm(forms.ModelForm):
    class Meta:
        model = AntecedentesSanitarios
        fields = ['contacto_estrecho',
                  'sintoma_fiebre',
                  'sintoma_perdida_olfato',
                  'sintoma_perdida_gusto',
                  'sintoma_tos',
                  'sintoma_dolor_garganta',
                  'sintoma_secrecion_nasal',
                  'sintoma_respiratorio',
                  'sintoma_aumento_frecuencia',
                  'sintoma_dolor_toracico',
                  'sintoma_dolor_muscular',
                  'sintoma_dolor_cabeza',
                  'sintoma_fatiga',
                  'sintoma_escalofrios',
                  'sintoma_diarrea',
                  'sintoma_nausea_vomitos',
                  'sintoma_otro',
                  'declaracion_confirmar',
                  'declaracion_archivo']
        labels = {
            'declaracion_confirmar': 
            """<em>DECLARO QUE NO SOY UN CASO ACTIVO CONFIRMADO DE COVID-19, TAMPOCO CALIFICO COMO CASO SOSPECHOSO NI PROBABLE, 
            DE ACUERDO A LO ESTABLECIDO EN LA NORMA SANITARIA, COMO LO REFIERE EL TÍTULO VI, Nº3, LETRAS a), b), c) y d) DE ESTE PROTOCOLO, 
            POR LO QUE ESTOY EN CONDICIONES DE SALUD ÓPTIMAS Y ADECUADAS PARA INGRESAR A LAS ACTIVIDADES DE PRÁCTICA PROFESIONAL Y/O 
            ACTIVIDADES CURRICULARES PRESENCIALES EN EL CAMPUS, SIN REPRESENTAR UN RIESGO PARA OTROS. 
            DECLARO QUE MIS ANTECEDENTES ACTUALES DE SALUD SON LOS DECLARADOS ANTERIORMENTE</em>
            """,
            'declaracion_archivo': "Archivo",
        }
        widgets = {
            'contacto_estrecho': forms.Select(attrs={'class': 'form-select'}),
            'sintoma_fiebre': forms.CheckboxInput(),
            'sintoma_perdida_olfato': forms.CheckboxInput(),
            'sintoma_perdida_gusto': forms.CheckboxInput(),
            'sintoma_tos': forms.CheckboxInput(),
            'sintoma_dolor_garganta': forms.CheckboxInput(),
            'sintoma_secrecion_nasal': forms.CheckboxInput(),
            'sintoma_respiratorio': forms.CheckboxInput(),
            'sintoma_aumento_frecuencia': forms.CheckboxInput(),
            'sintoma_dolor_toracico': forms.CheckboxInput(),
            'sintoma_dolor_muscular': forms.CheckboxInput(),
            'sintoma_dolor_cabeza': forms.CheckboxInput(),
            'sintoma_fatiga': forms.CheckboxInput(),
            'sintoma_escalofrios': forms.CheckboxInput(),
            'sintoma_diarrea': forms.CheckboxInput(),
            'sintoma_nausea_vomitos': forms.CheckboxInput(),
            'sintoma_otro': forms.TextInput(attrs={'class': 'form-control'}),
            'declaracion_confirmar': forms.CheckboxInput(attrs={'required': True}),
            'declaracion_archivo': forms.FileInput(attrs={'required': True}),
        }


class ActividadGeneralForm(forms.ModelForm):
    class Meta:
        model = ActividadGeneral
        fields = ['fecha', 
                  'hora_inicio',
                  'hora_fin',
                  'dependencia',
                  'descripcion']
        widgets = {
            'fecha': forms.TextInput(attrs={'class': 'form-control'}),
            'hora_inicio': forms.TextInput(attrs={'class': 'form-control'}),
            'hora_fin': forms.TextInput(attrs={'class': 'form-control',}),
            'dependencia': forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion': forms.TextInput(attrs={'class': 'form-control'}),
        }


class EventosForm(forms.ModelForm):
    class Meta:
        model = ActividadAcademica
        fields = ['fecha',
                  'hora_inicio',
                  'hora_fin',
                  'aula',
                  'asignatura',
                  'docente',
                  'facultad',
                  'carrera']

""" class ActividadAcademicaForm(ModelForm):    
    contatto_choice = forms.ModelChoiceField(queryset=ActividadAcademica.objects.all())
    class Meta:
        model = AntecedentesAcademicos
        fields = ['fecha',
                  'hora_inicio',
                  'hora_fin',
                  'aula',
                  'asignatura',
                  'docente',
                  'facultad',
                  'carrera'] """

class ActividadAcademicaForm(forms.Form):
    eventos = forms.ModelMultipleChoiceField(queryset=None)
    widgets = {
            'eventos': forms.TextInput(
                attrs={'class': 'form-control'}),
        }
    class Meta:
        model = AntecedentesAcademicos

    def __init__(self, *args, **kwargs):
        self.fields['eventos'].queryset = ActividadAcademica.objects.all()
        super().__init__(*args, **kwargs)
    
     


""" class ActividadAcademicaForm(forms.Form): 
    
    eventos = forms.ChoiceField(widget=forms.Select())

    def __init__(self, *args, **kwargs):
        super(forms.Form, self).__init__(*args, **kwargs)
        self.fields['eventos'].choices = [ l.hora_inicio for l in ActividadAcademica.objects.all()] """


class Register(forms.ModelForm):
    class Meta:
        model = Register_in_out
        fields = [
                'rut',
                'fecha',
                'hora',
                ]
        widgets = {
            'rut_visita': forms.TextInput(attrs={'class': 'form-control'}),
            'fecha': forms.TextInput(attrs={'class': 'form-control'}),
            'hora': forms.TextInput(attrs={'class': 'form-control',}),
        }