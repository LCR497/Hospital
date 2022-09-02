from django.shortcuts import render
from .models import *
def index(request):
    doctors = Doctor.objects.all()
    nurses = Nurse.objects.all()
    context = {
        'doctors': doctors,
        'nurses': nurses,
    }
    return render(request, 'index.html', context=context)

def patients(request):
    patient = Patient.objects.all()
    context = {
        'patients': patient
    }
    return render(request, 'patients.html', context=context)
