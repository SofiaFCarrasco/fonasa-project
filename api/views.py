from rest_framework.response import Response
from rest_framework.decorators import api_view
from api.serializers import PatientSerializer
from app.models import Patient

@api_view(['GET'])
def getPatients(request):
    patients = Patient.objects.all()
    serializer = PatientSerializer(patients, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getKidPatients(request):
    patients = Patient.objects.filter(patient_type = 1)
    serializer = PatientSerializer(patients, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getYoungPatients(request):

    patients = Patient.objects.filter(patient_type = 2)
    serializer = PatientSerializer(patients, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getOldPatients(request):
    patients = Patient.objects.filter(patient_type = 3)
    serializer = PatientSerializer(patients, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getYoungPatients(request):
    patients = Patient.objects.all()
    serializer = PatientSerializer(patients, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def addPatient(request):
    serializer = PatientSerializer(data=request.data)
    print(request.data)
    
    return Response(serializer.data) 

def calculateKidPriority():
    order = []
    kids = Patient.objects.filter(patient_type = 1)
    if kids:
        for kid in kids:
            if kid.age >= 1 and kid.age <=5:
                priority = kid.height_weight + 3
            elif kid.age >= 6 and kid.age <=12:
                priority = kid.height_weight + 2
            else:
                priority = kid.height_weight + 1
            kid.priority = priority

            kid.risk = kid.age * kid.priority / 100

            order.append(kid)
    
    return order



def calculateYoungPriority():
    order = []
    youngs = Patient.objects.filter(patient_type = 2)
    if youngs:
        for young in youngs:
            if young.smoker != 0:
                priority = young.smoker/4 + 2
            else:
                priority = 2
            young.priority = priority

            young.risk = young.age * young.priority / 100

            order.append(young)
    
    return order

def calculateElderPriorityAndRisk():
    order = []
    elders = Patient.objects.filter(patient_type = 2)
    if elders:
        for elder in elders:
            if elder.diet and elder.age >= 60 and elder.age <= 100:
                priority = elder.age/20 + 4
            else:
                priority = elder.age/30 + 3
            elder.priority = priority

            elder.risk = elder.age * elder.priority / 100 + 5.3

            order.append(elder)
    
    return order
