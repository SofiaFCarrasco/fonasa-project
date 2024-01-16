from django.http.response import JsonResponse
from django.shortcuts import render
from .models import *

# Create your views here.


def index(request):
    return render(request, 'index.html')


def list_patient(_request):
    patients = list(Patient.objects.values())
    data = {'patients': patients}
    return JsonResponse(data)