from collections import OrderedDict

from django.contrib.auth.models import User
from rest_framework import serializers

from .models import Tags, TextSnippets


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


class TextSnippetsSerializer(serializers.ModelSerializer):
    tags = serializers.ListField(
        child=serializers.CharField(), write_only=True
    )
    detail_view = serializers.SerializerMethodField()

    def validate_tags(self, value: list[str]) -> list[Tags]:
        if value:
            return list(map(lambda x: Tags.objects.get_or_create(title=x.lower())[0], value))
        raise serializers.ValidationError('Atleast one tag required')

    def get_detail_view(self, instance: TextSnippets) -> str:
        from rest_framework.request import Request

        request: Request = self.context.get('request')
        return f'{request.scheme}://{request.get_host()}/text_snippets/{instance.id}'

    class Meta:
        model = TextSnippets
        fields = '__all__'
        read_only_fields = ('slug', 'created_at', 'created_user')

    def save(self, **kwargs):
        kwargs['created_user'] = self.context.get('request').user
        return super().save(**kwargs)

    def to_representation(self, instance: TextSnippets) -> OrderedDict:
        data = super().to_representation(instance)
        data['tags'] = list(
            instance.tags.all().values_list('title', flat=True)
        )
        return data
