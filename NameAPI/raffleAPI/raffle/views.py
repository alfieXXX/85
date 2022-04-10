from django.shortcuts import render
from rest_framework import viewsets
from .models import rafflePeople
from .serializers import rpSerializer

# Create your views here.
class ViewRP(viewsets.ModelViewSet):
    queryset = rafflePeople.objects.all()
    serializer_class = rpSerializer