from django import forms
from .models import AntecedentesSanitarios


class RegisterForm(forms.ModelForm):
    class Meta:
        model = AntecedentesSanitarios
        fields = ['enfermedad_autoinmune',
                  'enfermedad_cronica',
                  'sintoma_fiebre',
                  'sintoma_perdida_olfato',
                  'sintoma_perdida_gusto',
                  'sintoma_tos',
                  'sintoma_dolor_garganta',
                  'sintoma_secrecion_nasal',
                  'sintoma_respiratorio',
                  'sintoma_aumento_frecuencia',
                  'sintoma_diarrea',
                  'sintoma_nausea_vomitos',
                  'sintoma_otro',
                  'embarazo',
                  'declaracion_confirmar',
                ]