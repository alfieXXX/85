from rest_framework import fields, serializers
from .models import ListDetail
from django.contrib.auth.models import User

class ListUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = ListDetail
        fields = '__all__'

        # extra_kwargs = {'password': {
        #     'write-only': True,
        #     'required': True
        # }}

class UsersSerializer(serializers.ModelSerializer):
    class Meta: 
        model = User
        feilds = ['id', 'username', 'password']


