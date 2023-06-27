from rest_framework import serializers, viewsets
from .models import Temp

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Temp
        fields =["amp", "data"]