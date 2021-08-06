from django.contrib import admin
from .models import (AntecedentesAcademicos, ActividadAcademica,
                     ActividadGeneral, AntecedentesPersonales, AntecedentesSanitarios,
                     Estudiante
                    )

admin.site.register(AntecedentesAcademicos)
admin.site.register(ActividadAcademica)
admin.site.register(ActividadGeneral)
admin.site.register(AntecedentesPersonales)
admin.site.register(AntecedentesSanitarios)
admin.site.register(Estudiante)