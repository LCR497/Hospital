from django.urls import path, include
from .views import *


urlpatterns = [
    path('login/',  loginPage, name='login'),
    path("register/", register_request, name="register"),
    path('api/v1/base-auth/', include('rest_framework.urls')),
    path('',  index, name='index'),
    path('patients/', patients, name='patients'),
    path('docdetail/<int:pk>', docDetail, name='docdetail'),
    path('logout/', logoutUser, name='logout'),
    path('api/v1/hospital/list/', HospitalListAPIView.as_view(), name='hospital'),
    path('api/v1/patient/list/', PatientListAPIView.as_view()),
    path('api/v1/nurse/list/', NurseListAPIView.as_view()),
    path('api/v1/chief/list/', ChiefPhysicianListAPIView.as_view()),
    path('api/v1/doctor/list/', DoctorListAPIView.as_view()),
    path('api/v1/user/register/', RegisterApiView.as_view()),
    path('api/v1/hospital/update/<int:pk>', HospitalUpdateAPIView.as_view()),
    path('api/v1/patient/update/<int:pk>', PatientUpdateAPIView.as_view()),
    path('api/v1/nurse/update/<int:pk>', NurseUpdateAPIView.as_view()),
    path('api/v1/chief/update/<int:pk>', ChiefPhysicianUpdateAPIView.as_view()),
    path('api/v1/doctor/update/<int:pk>', DoctorUpdateAPIView.as_view()),

]
