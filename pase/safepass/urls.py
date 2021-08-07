from django.urls import path
from safepass import views

app_name = "safepass"

urlpatterns = [
    path('', views.check, name="check"),
]