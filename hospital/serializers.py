from rest_framework import serializers
from .models import Hospital, Nurse, Patient, Doctor, Chief_Physician

class HospitalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hospital
        fields = '__all__'

class NurseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Nurse
        fields = '__all__'

class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = '__all__'

class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = '__all__'

class ChiefPhysicianSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chief_Physician
        fields = '__all__'
