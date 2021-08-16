from django.urls import path
from safepass import views

app_name = "safepass"

urlpatterns = [
    path('', views.check, name="check"),
    path('check/', views.check_form, name="check_form"),
    path('students/', views.students_form, name="students"),
    # path('students/<int:pk>/', views.students_form, name="students"),
    path('visitors/', views.visitors_form, name="visitors"),
    #path('pdf/', views.render_pdf_view, name="permission-pdf"),
    path('in-out/', views.descarga_tu_pdf, name="descarga"),
    path('eventos-programados/', views.eventos_programados, name='eventos-programados'),
    path('carreras/', views.carreras, name='carreras'),

]