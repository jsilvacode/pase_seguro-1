from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from .models import ( AntecedentesAcademicos, ActividadAcademica,
                     ActividadGeneral, AntecedentesPersonales, AntecedentesSanitarios,
                     Estudiante, Visita, Register_in_out, Carrera, Facultad
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
admin.site.register(Register_in_out)
admin.site.register(Visita)
admin.site.register(Carrera)
admin.site.register(Facultad)
