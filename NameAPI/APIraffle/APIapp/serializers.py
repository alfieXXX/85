from rest_framework import serializers
from .models import raf

class rpSerializer(serializers.ModelSerializer):
    class Meta:
        model = raf
        fields = '__all__'