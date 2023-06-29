from django.shortcuts import render
from rest_framework import viewsets
from .models import Temp
from. serializers import ClienteSerializer
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .serializers import ClienteSerializer, ClienteSerializer2
from datetime import datetime, timedelta
from .forms import temp_form


# Create your views here.

def index(request):
    return render(request, 'home.html')

def create_view(request):
    context = {}
    form = temp_form(request.POST or None)
    if form.is_valid():
        form.save()

    context['form'] = form
    return render(request, 'create_view.html', context)

def grafico_hora(request):
    ahora= datetime.now()
    data = []
    labels =[]
    ultima_hora = ahora-timedelta(hours=1)
    queryset = Temp.objects.all()
    for model in queryset:
        data.append(model.amp)
        labels.append(str(model.data.strftime("%Y-%m-%d %H:%M")))
    return render(request, 'grafico.html', {'labels': labels,'data': data})


@csrf_exempt
def Temp_serializer_agregar_data(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        snippets = Temp.objects.all()
        serializer = ClienteSerializer(snippets, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ClienteSerializer2(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)