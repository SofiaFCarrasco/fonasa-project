from django.urls import path
from . import views

urlpatterns = [
    path('get-patients/', views.getPatients),
    path('add-patient/', views.addPatient),
    path('get-kid-patient/', views.getKidPatients),
    path('get-young-patient/', views.getYoungPatients),
    path('get-old-patient/', views.getOldPatients),
]