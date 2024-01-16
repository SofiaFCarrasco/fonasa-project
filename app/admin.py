from django.contrib import admin
from app.models import *

# Register your models here.
admin.site.register(Hospital)
admin.site.register(Patient_Type)
admin.site.register(Specialist_Type)
admin.site.register(Consultation_Status)
admin.site.register(Patient)
admin.site.register(Specialist)
admin.site.register(Medical_Consultation)