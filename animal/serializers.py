from django.contrib.auth.models import User
from rest_framework import serializers

from .models import Animal


class AnimalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Animal
        fields = ['weight', 'length']
