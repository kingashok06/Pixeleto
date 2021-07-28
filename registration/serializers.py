from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from registration.models import User


def UserSerializers(ModelSerializer):
    class Meta:
        model = User
        fields = {'first_name', 'last_name' , 'phone_number' , 'email' }

        def validate(self, attrs):
            email = attrs.get('email', '')
            if User.objects.filter(email=email).exists():
                raise serializers.ValidationError(
                    {'email': ('Email is already in use')})
            return super().validate(attrs)

        def create(self, validated_data):
            return User.objects.create_user(**validated_data)
