from django.conf import settings
from django.http.response import Http404
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.template.loader import get_template
from .forms import (PerfilForm, EducacionForm, DeclaracionForm, EventosForm,
                    ActividadGeneralForm)
from .models import (AntecedentesPersonales, ActividadAcademica, Visita, Estudiante,
                     ActividadGeneral)
import  datetime 
from xhtml2pdf import pisa

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
    return render(request, "safepass/check_form.html")#, {'personal_fields': personal_fields})

def busqueda_sintomas_no_cardinales(request):

    lista_de_sintomas = [
        'contacto_estrecho', 'sintoma_tos', 'sintoma_dolor_garganta', 'sintoma_secrecion_nasal',
        'sintoma_respiratorio', 'sintoma_aumento_frecuencia', 'sintoma_dolor_toracico',
        'sintoma_dolor_muscular', 'sintoma_dolor_cabeza', 'sintoma_fatiga', 'sintoma_escalofrios',
        'sintoma_diarrea', 'sintoma_nausea_vomitos']
    lista = []
    for x in lista_de_sintomas:
        a = request.POST.get(x)
        if a:
            lista.append(a)
    if len(lista) <= 2:
        return False 
    else:
        return True

def busqueda_sintomas_cardinales(request):

    lista_de_sintomas = ['sintoma_fiebre','sintoma_perdida_olfato', 'sintoma_perdida_gusto']
    lista = []
    for x in lista_de_sintomas:
        a = request.POST.get(x)
        if a:
            lista.append(a)
    if len(lista) >= 1:
        return True 
    else:
        return False


def students_form(request):
    hoy = datetime.date.today()
    pasado = datetime.date.today() + datetime.timedelta(days=2)
    lista = ActividadAcademica.objects.all()
    events_forty_eigth = []
    for event in lista:
        if event.fecha <= pasado:
            if event.fecha >= hoy:
                events_forty_eigth.append(event)
    

    a =  request.POST.get('contacto_estrecho')
    if a == "si":
        return render(request, "safepass/exit.html")
    
    if request.method == "POST":
        if busqueda_sintomas_cardinales(request):
            return render(request, "safepass/exit.html")
        if busqueda_sintomas_no_cardinales(request):
            return render(request, "safepass/exit.html")

    if request.method == "POST":
        profile_form = PerfilForm(request.POST)
        if profile_form .is_valid():
                data1 = profile_form.save(commit=False)
                data1.save()
    if request.method == "POST":
        education_form = EducacionForm(request.POST)
        if education_form .is_valid():
                data2 = education_form.save(commit=False)
                data2.save()
    if request.method == "POST":
        statement_form = DeclaracionForm(request.POST, request.FILES)
        if profile_form.is_valid():
                data3 = statement_form.save(commit=False)
                data3.save()
    if request.method == "POST":
        id = request.POST['name']
        data4 = ActividadAcademica.objects.get(id=int(id))

    if  request.method=="POST":
        a = Estudiante.objects.create(
            antecedente_personal=data1,
            antecedente_academico=data2,
            actividad_academica=data4,
            antecedente_sanitario=data3
            )
        a.save()
        permission = a
        #pk = int(a.id)
        #render_pdf_view(request, pk)
        return render(request, "safepass/permission.html", {'permission': permission})
    
    profile_form = PerfilForm()
    education_form = EducacionForm()
    statement_form = DeclaracionForm()
    events_form = EventosForm()
    # ----
    return render(request, "safepass/students.html", {
        'profile_form': profile_form, 'education_form': education_form, 
        'statement_form': statement_form, 'events_form': events_form, 
        'events_forty_eigth': events_forty_eigth
    })


def visitors_form(request):
    hoy = datetime.date.today()
    pasado = datetime.date.today() + datetime.timedelta(days=2)
    lista = ActividadAcademica.objects.all()
    events_forty_eigth = []
    for event in lista:
        if event.fecha <= pasado:
            if event.fecha >= hoy:
                events_forty_eigth.append(event)

    a =  request.POST.get('contacto_estrecho')
    if a == "si":
        return render(request, "safepass/exit.html")
    
    if request.method == "POST":
        if busqueda_sintomas_cardinales(request):
            return render(request, "safepass/exit.html")
        if busqueda_sintomas_no_cardinales(request):
            return render(request, "safepass/exit.html")

    if request.method == "POST":
        profile_form = PerfilForm(request.POST)
        if profile_form .is_valid():
                data1 = profile_form.save(commit=False)
                data1.save()
    if request.method == "POST":
        statement_form = DeclaracionForm(request.POST)
        if statement_form .is_valid():
                data2 = statement_form.save(commit=False)
                data2.save()
    if request.method == "POST":
        activity_general = ActividadGeneralForm(request.POST, request.FILES)
        if activity_general.is_valid():
                data3 = activity_general.save(commit=False)
                data3.save()
    if  request.method=="POST":
        a = Visita.objects.create(
            antecedente_personal=data1,
            antecedente_sanitario=data2,
            actividad_general=data3
            )
        a.save()
        permission = a
        return render(request, "safepass/permission.html", {'permission': permission})
    
    profile_form = PerfilForm()
    statement_form = DeclaracionForm()
    activity_general = ActividadGeneralForm()
    # ----
    return render(request, "safepass/visitors.html", {
        'profile_form': profile_form, 'statement_form': statement_form, 
        'activity_general': activity_general, 'activities_forty_eigth': activities_forty_eigth
    })

def link_callback(uri, rel):
    """
    Convert HTML URIs to absolute system paths so xhtml2pdf can access those
    resources
    """
    sUrl = settings.STATIC_URL        # Typically /static/
    mUrl = settings.MEDIA_URL         # Typically /media
    path = ''

    if uri.startswith(mUrl):
        path = "{}{}".format(settings.BASE_DIR._str, uri)
    elif uri.startswith(sUrl):
        path = "{}{}".format(settings.BASE_DIR._str, uri)
    else:
        return uri

    return path

def render_pdf_view(request, *args, **kwargs):
    #permission = get_object_or_404(StatementOfConditions, pk=kwargs.get('pk'))
    if Visita.objects.get(id=id):
        permission = Visita.objects.get(id=id)
    if Estudiante.objects.get(id=id):
        permission = Estudiante.objects.get(id=id)
    context = {'permission': permission}

    template_path = 'SanitaryRegulations/permission_pdf_template.html'
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')

    # download
    # response['Content-Disposition'] = 'attachment; filename="report.pdf"'

    # display
    response['Content-Disposition'] = 'filename="permission.pdf"'

    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(html, dest=response, link_callback=link_callback)
    # if error then show some funy view
    if pisa_status.err:
        return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response
