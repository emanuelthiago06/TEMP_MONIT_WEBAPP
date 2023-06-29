from rest_framework import serializers, viewsets
from .models import Temp

class ClienteSerializer(serializers.ModelSerializer): #GET
    class Meta:
        model = Temp
        fields =["amp", "data"]

class ClienteSerializer2(serializers.ModelSerializer): #POST
    class Meta:
        model = Temp
        fields = ["amp"]