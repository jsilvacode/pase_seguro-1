from django.http.response import Http404
from django.shortcuts import render
from .forms import (PerfilForm, EducacionForm, DeclaracionForm, ActividadAcademicaForm )
from .models import AntecedentesPersonales, Visita, ActividadAcademica


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
        if statement_form.is_valid():
                data = statement_form.save(commit=False)
                data.save()
    if request.method == "POST":
        activity_form = ActividadAcademicaForm(request.POST, request.FILES)
        if activity_form.is_valid():
            data = activity_form.save(commit=False)
            data.save()
    
    profile_form = PerfilForm()
    education_form = EducacionForm()
    statement_form = DeclaracionForm()
    activity_form = ActividadAcademicaForm()
    # ----
    
    return render(request, "safepass/students.html", {
        'profile_form': profile_form, 'education_form': education_form, 
        'statement_form': statement_form, 'activity_form': activity_form
    })


def visitors_form(request):
    return render(request, "safepass/visitors.html")


def render_pdf_view(request):
    return render(request, "safepass/permission.html")



""" form_tournament = TournamentCreationForm(request.POST or None)
    form_sport  = SportEditForm(request.POST or None)
    if form_tournament.is_valid() and form_sport.is_valid():
    instance = form_tournament.save(commit=False)
    instance.user = request.user
    instance.save() """