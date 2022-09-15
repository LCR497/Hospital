from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from .forms import *
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from .serializers import HospitalSerializer, NurseSerializer, PatientSerializer, ChiefPhysicianSerializer, DoctorSerializer, UserSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, CreateAPIView
from rest_framework.permissions import IsAuthenticated, IsAdminUser
def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username , password=password)

        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.info(request, 'Неправильный Логин или Пароль')
    context = {}
    return render(request, 'login.html', context)

def logoutUser(request):
    logout(request)
    return redirect('index')


def register_request(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful.")
            return redirect("login")
        messages.error(request, "Unsuccessful registration. Invalid information.")
    form = NewUserForm()
    return render(request, "signup.html", context={"register_form": form})



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
        'doctor' : doc
    }
    return render(request, 'docdetail.html', context=context)


class HospitalListAPIView(ListCreateAPIView):
    queryset = Hospital.objects.all()
    serializer_class = HospitalSerializer
    # permission_classes = [IsAuthenticated, ]

class DoctorListAPIView(ListCreateAPIView):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
    # permission_classes = [IsAuthenticated, ]

class NurseListAPIView(ListCreateAPIView):
    queryset = Nurse.objects.all()
    serializer_class = NurseSerializer
    # permission_classes = [IsAuthenticated, ]

class PatientListAPIView(ListCreateAPIView):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer
    # permission_classes = [IsAuthenticated, ]

class ChiefPhysicianListAPIView(ListCreateAPIView):
    queryset = Chief_Physician.objects.all()
    serializer_class = ChiefPhysicianSerializer
    # permission_classes = [IsAuthenticated, ]

class HospitalUpdateAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Hospital.objects.all()
    serializer_class = HospitalSerializer
    # permission_classes = [IsAuthenticated, ]


class DoctorUpdateAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
    # permission_classes = [IsAuthenticated, ]

class NurseUpdateAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Nurse.objects.all()
    serializer_class = NurseSerializer
    # permission_classes = [IsAuthenticated, ]

class PatientUpdateAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer
    # permission_classes = [IsAuthenticated, ]

class ChiefPhysicianUpdateAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Chief_Physician.objects.all()
    serializer_class = ChiefPhysicianSerializer
    # permission_classes = [IsAuthenticated, ]

class RegisterApiView(CreateAPIView):
    queryset = user.objects.all()
    serializer_class = UserSerializer




