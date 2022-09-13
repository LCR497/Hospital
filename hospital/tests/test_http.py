from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from hospital.models import Hospital
from hospital.serializers import HospitalSerializer



class Http200TestCase(APITestCase):
    def test_get(self):
        url = 'http://127.0.0.1:8000/'
        url = reverse('index')
        print(url)
        response = self.client.get(url)
        url = reverse('index')
        print(url)
        self.assertEqual(status.HTTP_200_OK, response.status_code)

class Http400HospitalTestCase(APITestCase):
    def test_get(self):
        url = 'http://127.0.0.1:8000'
        url = reverse('apihospital')
        data = {
            'okpo': 155,
            'region' : '1',
            "employees" : '200',
            'state_or_private' : '1'
        }
        response = self.client.post(url,data=data)
        print(response.data)
        print(response.status_code)
        self.assertEqual(status.HTTP_400_BAD_REQUEST, response.status_code)

class Http201HospitalTestCase(APITestCase):
    def test_create(self):
        url = 'http://127.0.0.1:8000'
        url = reverse('apihospital')
        data = {
            'okpo': 155,
            'region' : '1',
            "employees" : '200',
            'state_or_private' : 'государственная'
        }
        response = self.client.post(url,data=data)
        print(response.data)
        print(response.status_code)
        self.assertEqual(status.HTTP_201_CREATED, response.status_code)

class Http405HospitalTestCase(APITestCase):
    def test_delete(self):
        url = 'http://127.0.0.1:8000'
        url = reverse('apihospital')
        data = {
            'okpo': 155,
            'region' : '1',
            "employees" : '200',
            'state_or_private' : 'государственная'
        }
        response = self.client.delete(url, data=data)
        print(response.data)
        print(response.status_code)
        self.assertEqual(status.HTTP_405_METHOD_NOT_ALLOWED, response.status_code)

class Http404TestCase(APITestCase):
    def test_not_found(self):
        url = 'http://127.0.0.1:8000/as'
        response = self.client.get(url)
        self.assertEqual(status.HTTP_404_NOT_FOUND, response.status_code)