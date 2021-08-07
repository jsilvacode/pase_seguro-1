from django.shortcuts import render


def check(request):
    return render(request, "safepass/check.html")


def students_form(request):
    return render(request, "safepass/students.html")
