from django.urls import path
from safepass import views

app_name = "safepass"

urlpatterns = [
    path('', views.check, name="check"),
    path('students/', views.students_form, name="students"),
    path('students/<int:student_id>', views.students_form, name="students")
]