from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import (TemplateView)
from django.db import transaction
from .serializers import UserSerializer, rpSerializer
from .models import MUser, rafflePeople
from rest_framework import viewsets
import json                                

class Signup(TemplateView):
    template_name='signup/signup.html'   

class ViewRP(viewsets.ModelViewSet):
    queryset = rafflePeople.objects.all()
    serializer_class = rpSerializer