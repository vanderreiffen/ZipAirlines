from django.shortcuts import render
from rest_framework import viewsets, generics
from .serializers import AircraftSerializer
from airlines.models import Aircraft
# Create your views here.

class AirCraftAPIView(viewsets.ModelViewSet):

    queryset = Aircraft.objects.all()
    serializer_class =AircraftSerializer
