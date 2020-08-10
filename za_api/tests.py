from django.test import TestCase, Client
import json
from django.urls import reverse
from rest_framework import status
from .models import Airplane
from .serializers import AirplaneSerializer

#init client

client = Client()
#model
class AirplaneTestCase(TestCase):

    def setUp(self):
        Airplane.objects.create(uid=3, passenger_capacity= 600)
        Airplane.objects.create(uid=5, passenger_capacity= 1200)

    #model fields    
    def test_air_plane_fuel(self):
        #assess if the fuel capacity is correct based on the uid
        airplane_fuel1 =Airplane.objects.get(uid=3)
        airplane_fuel2 =Airplane.objects.get(uid=5)
        
        self.assertEqual(airplane_fuel1.fueltank_cap, 600)
        self.assertEqual(airplane_fuel2.fueltank_cap, 1000)
    

    def test_air_plane_consumption_per_minute(self):
        airplane_fuel1 =Airplane.objects.get(uid=3)
        airplane_fuel2 =Airplane.objects.get(uid=5)
        self.assertEqual(airplane_fuel1.consumption_per_minute, 0.8789)
        self.assertEqual(airplane_fuel2.consumption_per_minute, 1.2876)

    def test_max_minutes(self):
        a1 = Airplane.objects.get(uid =3)
        a2 = Airplane.objects.get(uid =5)
        self.assertEqual(a1.max_minutes, 683.879419970128)
        self.assertEqual(a2.max_minutes, 779.0686681995147)

    #api
    def test_get_all_airplanes(self):
        #get api response
        response = client.get(reverse('airline-api'))
        all_planes = Airplane.objects.all()
        serializer = AirplaneSerializer(all_planes, many=True)
        self.assertEqual(response.data , serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def tearDown(self):
        a1 = Airplane.objects.get(uid=3)
        a2 = Airplane.objects.get(uid=5)
        a1.delete()
        a2.delete()
