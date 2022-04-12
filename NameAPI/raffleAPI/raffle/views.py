from django.shortcuts import render
from rest_framework import viewsets
from .models import raf
from .serializers import rpSerializer

# Create your views here.
class ViewRP(viewsets.ModelViewSet):
    queryset = raf.objects.all()
    serializer_class = rpSerializer