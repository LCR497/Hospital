from .models import *
from django import forms

class DoctorDetail(forms.ModelForm):

    class Meta:
        model = Doctor
        fields = ('type_dr', 'full_name', 'pin_code', 'age', 'phone_number', 'nurse', 'hospital', )

