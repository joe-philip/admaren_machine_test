from django.contrib.auth.models import User
from rest_framework import serializers


class UserSignupSerializer(serializers.ModelSerializer):
    def validate_email(self, value: str) -> str:
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError('Email already exists')
        return value

    class Meta:
        model = User
        exclude = ('is_staff', 'is_active', 'date_joined')
        extra_kwargs = {
            'password': {'write_only': True},
            'first_name': {'required': True},
            'email': {'required': True}
        }

    def save(self, **kwargs) -> User:
        self.instance = User.objects.create_user(**self.validated_data)
        return self.instance
