from django.contrib import admin
from .models import *


class PatientAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'pin_code', 'age', 'phone_number')

class NurseAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'pin_code', 'age', 'phone_number')

class HospitalAdmin(admin.ModelAdmin):
    list_display = ('okpo', 'region', 'state_or_private')

class Chief_PhysicianAdmin(admin.ModelAdmin):
    list_display = ('hospital', 'full_name', 'pin_code', 'age', 'phone_number')

class DoctorAdmin(admin.ModelAdmin):
    list_display = ('id','type_dr', 'full_name', 'pin_code', 'age', 'phone_number')

admin.site.register(Patient, PatientAdmin)
admin.site.register(Nurse, NurseAdmin)
admin.site.register(Doctor, DoctorAdmin)
admin.site.register(Chief_Physician, Chief_PhysicianAdmin)
admin.site.register(Hospital, HospitalAdmin)