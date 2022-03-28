from django.shortcuts import render

# Create your views here.
from django.http import response
from django.shortcuts import render
from rest_framework import serializers
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication 
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated

from apiApp.serializers import ListUserSerializer, UsersSerializer
from apiApp.models import ListDetail
from django.contrib.auth.models import User
from rest_framework import viewsets

class ListView(viewsets.ModelViewSet):
    queryset = ListDetail.objects.all().order_by('id')
    serializer_class = ListUserSerializer
    # authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAuthenticated]

class UserViewset(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UsersSerializer()
    # authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAuthenticated]

