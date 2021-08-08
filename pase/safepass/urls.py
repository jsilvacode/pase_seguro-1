from django.urls import path
from safepass import views

app_name = "safepass"

urlpatterns = [
    path('', views.check, name="check"),
    path('check/', views.check_form, name="check_form"),
    path('visitors/', views.visitors_form, name="visitors"),
    path('students/', views.students_form, name="students"),
    path('pdf/', views.render_pdf_view, name="permission-pdf"),
]