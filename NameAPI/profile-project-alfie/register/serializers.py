from rest_framework import serializers
from .models import MUser, rafflePeople

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = MUser
        fields = [
                     'firstname'
                     ,'date_updated'
                ]


class rpSerializer(serializers.ModelSerializer):
    class Meta:
        model = rafflePeople
        fields = '__all__'

        