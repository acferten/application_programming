from rest_framework import serializers

from .models import Animal, Type


class AnimalSerializer(serializers.ModelSerializer):
    lifeStatus = serializers.CharField(source='get_lifeStatus_display', read_only=True)
    gender = serializers.CharField(source='get_gender_display', read_only=True)
    chipperId = serializers.IntegerField(source='chipper.id', read_only=True)
    chippingLocationId = serializers.IntegerField(source='chippingLocation.id', read_only=True)

    class Meta:
        model = Animal
        exclude = ['chipper', 'chippingLocation']


class TypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Type
        fields = '__all__'
