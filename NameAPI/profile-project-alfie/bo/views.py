from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from django.shortcuts import render
from django.http import Http404
from django.views.generic import (TemplateView)
from django.db import transaction
from django.db.models import Value
from django.db.models.functions import Concat
from register.models import MUser
from register.serializers import UserSerializer
from .common import Repeated                            
import datetime
import json

class View(TemplateView):
    template_name='user/user.html'

class Transact(APIView):
    '''
        Author: Armando Garing II
        Date Created: Sept. 06, 2021
        Purpose: Responsible for user search
    '''    
    # permission_classes = (IsAuthenticated,)
    def get(self, request, format=None):
        value = Repeated()
        list_data={}
        result_data = {}

        search_value = request.GET.get('search_value', '')

        queryset = MUser.objects.annotate(
                                    search=Concat('firstname',Value(' '),'lastname')).filter(
                                    search__icontains=search_value) 
                                    
        list_data= queryset.values('user_id'
                        ,'firstname'
                        ,'lastname'
                        ,'reference_tablestatus_fk'                        
                        ,'reference_tablestatus_fk__reference_longdesc')
                                                                                                
        # return Response(list_data)
        if len(list_data):
            result_data['code'] = status.HTTP_200_OK
            result_data['message'] = value.http_message(status.HTTP_200_OK)
        else:
            result_data['code'] = status.HTTP_204_NO_CONTENT
            result_data['message'] = value.http_message(status.HTTP_204_NO_CONTENT)

        result_data['data'] = list_data

        return Response(result_data, status=status.HTTP_201_CREATED)      

    def get_object(self, pk):
        try:
            return MUser.objects.get(user_id=pk)
        except MUser.DoesNotExist:
            raise Http404  
   

    def put(self, request, pk, format=None):
        value = Repeated()
        user_id = self.get_object(pk)
        result = {}

        data = json.dumps(request.data)
        form = json.loads(data)

        form['user_id'] = user_id
        form['date_updated'] = datetime.datetime.now()

        serialize = UserSerializer(user_id, data=form)
        if serialize.is_valid():
            serialize.save()

            result['data'] = serialize.data
            result['code'] = status.HTTP_200_OK
            result['message'] = value.http_message(status.HTTP_200_OK)            
            return Response(result, status=status.HTTP_201_CREATED)
        return Response(serialize.errors, status=status.HTTP_400_BAD_REQUEST)         