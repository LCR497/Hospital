from django.urls import path, include
from .views import *

urlpatterns = [
    path('login/',  loginPage, name='login'),
    path("register/", register_request, name="register"),
    path('api/v1/auth/', include('djoser.urls')),
    path('api/v1/auth-token/', include('djoser.urls.authtoken')),
    path('',  index, name='index'),
    path('patients/', patients, name='patients'),
    path('docdetail/<int:pk>', docDetail, name='docdetail'),
    path('logout/', logoutUser, name='logout'),
    path('api/v1/hospital/list/', HospitalListAPIView.as_view()),
    path('api/v1/pacient/list/', PatientListAPIView.as_view()),
    path('api/v1/nurse/list/', NurseListAPIView.as_view()),
    path('api/v1/chief/list/', ChiefPhysicianListAPIView.as_view()),
    path('api/v1/doctor/list/', DoctorListAPIView.as_view()),
    # path('api/v1/hospital/update/', HospitalUpdateAPIView.update())
    # path('api/v1/pacient/update/', PatientUpdateAPIView.update()),
    # path('api/v1/nurse/update/', NurseUpdateAPIView.update()),
    # path('api/v1/chief/update/', ChiefPhysicianUpdateAPIView.update()),
    # path('api/v1/doctor/update/', DoctorUpdateAPIView.as_view()),
]
