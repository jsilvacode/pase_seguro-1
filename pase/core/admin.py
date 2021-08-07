from django.contrib import admin
from .models import (AntecedentesAcademicos, ActividadAcademica,
                     ActividadGeneral, AntecedentesPersonales, AntecedentesSanitarios,
                     Estudiante, Visita
                    )


class ActividadAcademicaResource(resources.ModelResource):

    class Meta:
        model = ActividadAcademica


class ActividadAcademicaAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    resource_class = ActividadAcademicaResource

admin.site.register(AntecedentesAcademicos)
admin.site.register(ActividadAcademica, ActividadAcademicaAdmin)
admin.site.register(ActividadGeneral)
admin.site.register(AntecedentesPersonales)
admin.site.register(AntecedentesSanitarios)
admin.site.register(Estudiante)
admin.site.register(Visita)
