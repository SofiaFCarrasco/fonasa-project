from rest_framework.response import Response
from rest_framework.decorators import api_view
from api.serializers import PatientSerializer
from app.models import Patient

@api_view(['GET'])
def getPatients(request):
    patients = Patient.objects.all()
    serializer = PatientSerializer(patients, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def addPatient(request):
    serializer = PatientSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data) 