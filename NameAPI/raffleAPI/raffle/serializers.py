from rest_framework import serializers
from .models import rafflePeople

class rpSerializer(serializers.ModelSerializer):
    class Meta:
        model = rafflePeople
        fields = '__all__'