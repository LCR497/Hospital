from django.urls import path
from .views import *

urlpatterns = [
    path('',  loginPage, name='login'),
    path("register/", register_request, name="register"),
    path('index/',  index, name='index'),
    path('patients/', patients, name='patients'),
    path('docdetail/<int:pk>', docDetail, name='docdetail'),
    path('logout/', logoutUser, name='logout')
]
