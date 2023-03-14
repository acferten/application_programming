from django.contrib.auth.models import User
from rest_framework import serializers

from account.models import AdvUser


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdvUser
        fields = ['id', 'first_name', 'last_name', 'email']


class CreateAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdvUser
        fields = ['email', 'password', 'first_name', 'last_name']

    def create(self, validated_data):
        user = AdvUser.objects.create(
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            email=validated_data['email'],
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
