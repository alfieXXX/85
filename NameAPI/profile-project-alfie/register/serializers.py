from rest_framework import serializers
from .models import MUser

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = MUser
        fields = [
                     'firstname'
                     ,'date_updated'
                ]

       
               

        