from django.test import TestCase, Client
from django.urls import reverse
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Aircraft
from airlines.api.serializers import AircraftSerializer



#init client

client = Client()
#model value tests
class AirCraftTestCase(TestCase):

    def setUp(self):
        Aircraft.objects.create(user_defined_id=3, passenger_Cap= 600)
        Aircraft.objects.create(user_defined_id=5, passenger_Cap= 1200)
    #model fields    
    def test_air_plane_fuel(self):
        #assess if the fuel capacity is correct based on the user_defined_id
        aircraft_fuel1 =Aircraft.objects.get(user_defined_id=3)
        aircraft_fuel2 =Aircraft.objects.get(user_defined_id=5)
        
        self.assertEqual(aircraft_fuel1.fueltank_cap_liters, 600)
        self.assertEqual(aircraft_fuel2.fueltank_cap_liters, 1000)



    def tearDown(self):
        a1 = Aircraft.objects.get(user_defined_id=3)
        a2 = Aircraft.objects.get(user_defined_id=5)
        a1.delete()
        a2.delete()


class APIaircraftTest(TestCase):
    def setUp(self):
        self.valid_payload = {
            'user_defined_id' : 6,
            'passenger_Cap' : 500
        }
        self.invalid_payload = {
            'user_defined_id' : '',
            'passenger_Cap' : 'Hellow'
        }
    
    #CREATE VALID ENTRY
    def test_api_response(self):
        """
        Ensure we have access to API endpoint.
        """
        # url = 'http://127.0.0.1:8000/api/aircraft/'
        url = reverse('airlines:aircraft-list')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_valid_entry(self):
        """
        Ensure API can enter valid data.
        """
        url = reverse('airlines:aircraft-list')
        response = self.client.post(url, self.valid_payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['user_defined_id'], 6)
    


