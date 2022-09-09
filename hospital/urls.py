from django.urls import path
from .views import *

urlpatterns = [
    path('',  index, name='index'),
    path('patients/', patients, name='patients'),
    path('docdetail/<int:pk>', docDetail, name='docdetail')
]
