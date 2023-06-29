from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from appcore.views import Temp_serializer_agregar_data


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('',include('appcore.urls')),
]
