from django.http.response import Http404
from django.shortcuts import render
from .forms import (PerfilForm, EducacionForm, DeclaracionForm)
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
    if request.method == "POST":
        profile_form = PerfilForm(request.POST)
        if profile_form .is_valid():
                data = profile_form.save(commit=False)
                data.save()
    if request.method == "POST":
        education_form = EducacionForm(request.POST)
        if education_form .is_valid():
                data = education_form.save(commit=False)
                data.save()
    if request.method == "POST":
        statement_form = DeclaracionForm(request.POST, request.FILES)
        if profile_form.is_valid():
                data = statement_form.save(commit=False)
                data.save()
    
    profile_form = PerfilForm()
    education_form = EducacionForm()
    statement_form = DeclaracionForm()
    # ----
    return render(request, "safepass/students.html", {
        'profile_form': profile_form, 'education_form': education_form, 
        'statement_form': statement_form
    })


def visitors_form(request):
    return render(request, "safepass/visitors.html")


def render_pdf_view(request):
    return render(request, "safepass/permission.html")
