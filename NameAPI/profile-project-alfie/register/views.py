from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import (TemplateView)
from django.db import transaction
from .serializers import UserSerializer
from .models import MUser
import json                                

class Signup(TemplateView):
    template_name='signup/signup.html'   

class Save(APIView):
    def post(self, request, format=None):
        """
            Author: Armando Garing II
            Date Created: Feb. 02, 2022
        """      
        context = {}
        result_data = {}

        data = json.dumps(request.data)
        context = json.loads(data)

        with transaction.atomic():
            user_id = 1 if MUser.objects.count() == 0 else MUser.objects.last().user_id + 1

            context['user_id'] = user_id
            user = UserSerializer(data=context)

            if user.is_valid(raise_exception=True):
                user.save()

                result_data['code'] = status.HTTP_200_OK
                result_data['message'] = 'Successfully save'
                result_data['data'] = user.data
                return Response(result_data, status=status.HTTP_201_CREATED)   
            else:
                transaction.set_rollback(True)
                return Response(user.errors,
                                status=status.HTTP_400_BAD_REQUEST)     
 