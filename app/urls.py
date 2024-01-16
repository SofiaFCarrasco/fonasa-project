from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('list_patient/', views.list_patient, name='list_patient')
]