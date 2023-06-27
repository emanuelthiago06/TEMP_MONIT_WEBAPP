from django.shortcuts import render
from rest_framework import viewsets
from .models import Temp
from. serializers import ClienteSerializer

# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    queryset = Temp.objects.all()
    serializer_class = ClienteSerializer