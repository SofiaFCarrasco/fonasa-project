from django.urls import path
from . import views

urlpatterns = [
    path('get-patients/', views.getPatients),
    path('add-patient/', views.addPatient)
]