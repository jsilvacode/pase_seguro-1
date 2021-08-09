from django.http.response import Http404
from django.shortcuts import render
from .models import AntecedentesPersonales


def check(request):
    return render(request, "safepass/check.html")


def check_form(request):
    return render(request, "safepass/check_form.html")


"""
def check_form(request, student_id):
    try:
        personal_fields = AntecedentesPersonales.objects.get(id=student_id)
    except AntecedentesPersonales.DoesNotExist:
        raise Http404("Estudiante no registrado")
    return render(request, "safepass/check_form.html", {'personal_fields': personal_fields})
"""


def students_form(request):

    return render(request, "safepass/students.html")


def visitors_form(request):
    return render(request, "safepass/visitors.html")


def render_pdf_view(request):
    return render(request, "safepass/permission.html")
