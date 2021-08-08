from django.shortcuts import render, get_object_or_404
from .models import AntecedentesPersonales


def check(request):
    return render(request, "safepass/check.html")


def check_form(request):
    return render(request, "safepass/check_form.html")


def students_form(request):
    personal_info = get_object_or_404(AntecedentesPersonales)
    return render(request, "safepass/students.html",{'personal_info': personal_info})


def visitors_form(request):
    return render(request, "safepass/visitors.html")

def render_pdf_view(request):
    return render(request, "safepass/permission.html")
