from rest_framework import serializers
from .models import HelloModel

class HelloSerializer(serializers.ModelSerializer):
    class Meta:
        model = HelloModel
        fields = ['message']