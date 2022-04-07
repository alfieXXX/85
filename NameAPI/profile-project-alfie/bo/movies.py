from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import (TemplateView)
from django.db import transaction
# from register.serializers import UserSerializer
# from register.models import MUser
import json                                

class Movies(TemplateView):
    template_name='movies/movies.html'