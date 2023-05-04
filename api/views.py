from django.shortcuts import render
from rest_framework import viewsets
from .serializers import BootSerializer
from .models import Boot

# Create your views here.

class BootViewSet(viewsets.ModelViewSet):
    queryset= Boot.objects.all().order_by('modelName')
    serializer_class = BootSerializer

