from rest_framework import serializers

from .models import Animal


class AnimalSerializer(serializers.ModelSerializer):
    lifeStatus = serializers.CharField(source='get_lifeStatus_display', read_only=True)
    gender = serializers.CharField(source='get_gender_display', read_only=True)

    class Meta:
        model = Animal
        fields = '__all__'
