from django.shortcuts import render, get_object_or_404
from .models import *
from .forms import DoctorDetail
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

def docDetail(request, pk):
    doc = get_object_or_404(Doctor, pk=pk)
    context = {
        'doctor': doc
    }
    return render(request, 'docdetail.html', context=context)
