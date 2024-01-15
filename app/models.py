from django.db import models

# Create your models here.
class Hospital(models.Model):
    id = models.BigAutoField(primary_key=True)

class Patient_Type(models.Model):
    description = models.CharField(max_length=100)

class Specialist_Type(models.Model):
    description = models.CharField(max_length=100)

class Consultation_Status(models.Model):
    description = models.CharField(max_length = 100)

class Patient(models.Model) :
    rut = models.CharField(max_length=9,primary_key=True)
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    medical_history = models.BooleanField(default=False)
    diet = models.BooleanField(default = False)
    smoker = models.IntegerField ()
    height_weight = models.IntegerField()
    patient_type = models.ForeignKey(Patient_Type, on_delete=models.CASCADE)

class Specialist(models.Model):
    name = models.CharField(max_length = 50)
    specialist_type = models.ForeignKey(Specialist_Type, on_delete = models.CASCADE)

class Medical_Consultation(models.Model):
    patient = models.ForeignKey(Patient, on_delete = models.CASCADE)
    consultation_status = models.ForeignKey(Consultation_Status, on_delete = models.CASCADE)
    date = models.DateTimeField()
    specialist = models.ForeignKey(Specialist, on_delete = models.CASCADE)
    hospital = models.ForeignKey(Hospital, on_delete = models.CASCADE)