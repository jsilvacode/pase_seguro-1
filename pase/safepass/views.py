from django.http.response import Http404
from django.shortcuts import render
from .models import AntecedentesPersonales, ActividadAcademica, Visita
from datetime import date



def check(request):
    algo = ""
    return render(request, "safepass/check.html")


""" def check_form(request):
    algo = ""
    return render(request, "safepass/check_form.html") """



def check_form(request):
    try:
        if request.POST:
            a=request.POST['rut']
            id_visit = AntecedentesPersonales.objects.get(rut=a).id
            personal_fields = Visita.objects.filter(antecedente_personal_id=id_visit)
    except AntecedentesPersonales.DoesNotExist:
        raise Http404("Estudiante no registrado")
    return render(request, "safepass/check_form.html", {'personal_fields': personal_fields})



def students_form(request):
    today = date.today()
    all = ActividadAcademica.objects.all()
    for x in all:
        if x.fecha > today:
            print(x.fecha)
            print(x.hora_inicio)
            print(x.aula)
            print(x.docente)

    contexto = {}
    return render(request, "safepass/students.html",{"contexto":contexto})


def visitors_form(request):
    return render(request, "safepass/visitors.html")


def render_pdf_view(request):
    return render(request, "safepass/permission.html")
