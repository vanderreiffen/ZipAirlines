from django.shortcuts import render
from rest_framework import viewsets, generics
from .serializers import AirplaneSerializer
from .models import Airplane
# Create your views here.

class AirplaneViewSet(viewsets.ModelViewSet):

    queryset = Airplane.objects.all().order_by('uid')
    serializer_class =AirplaneSerializer
