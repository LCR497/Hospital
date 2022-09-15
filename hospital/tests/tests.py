from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from hospital.models import Hospital, Doctor, Nurse, Patient, Chief_Physician
from hospital.serializers import *

class HospitalApiTestCase(APITestCase):
    def test_hospital(self):
        url = 'http://127.0.0.1:4445/api/v1/base-auth/login/?next=/api/v1/hospital/list/'
        data = {'username': 'admin', 'password': 'admin'}
        response = self.client.post(url, data=data)
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        url = 'http://127.0.0.1:4445/api/v1/hospital/list/'
        data = {'okpo' : 24, 'region': 'Bishkek', 'employees': '100', 'state_or_private': 'частная'}
        response = self.client.post(url, data=data)
        self.assertEqual(status.HTTP_201_CREATED, response.status_code)
        url = 'http://127.0.0.1:4445/api/v1/hospital/update/1'
        data = {'okpo': 24, 'region': 'Bishkek', 'employees': '100', 'state_or_private': 'частная'}
        response = self.client.put(url, data=data)
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        response = self.client.delete(url, data=data)
        self.assertEqual(status.HTTP_204_NO_CONTENT, response.status_code)

    def test_doctor(self):
        url = 'http://127.0.0.1:4445/api/v1/base-auth/login/?next=/api/v1/hospital/list/'
        data = {'username':'admin', 'password': 'admin'}
        response = self.client.post(url, data=data)
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        url = 'http://127.0.0.1:4445/api/v1/doctor/list/'
        data = {'type_dr' : 'терапевт',
                'full_name':'Медсестра А А',
                'pin_code': '100',
                'age': 45,
                'experience': 30,
                'phone_number': '0444333222',
                'nurse': 1,
                'hospital': 1
                }
        response = self.client.post(url, data=data)
        print(response.data)

