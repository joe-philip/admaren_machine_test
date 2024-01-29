from django.db.models import QuerySet
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from .models import Tags, TextSnippets
from .serializers import (TagDetailSerializer, TagListSerializer,
                          TextSnippetsSerializer, UserSignupSerializer)

# Create your views here.


class SignupAPI(CreateAPIView):
    serializer_class = UserSignupSerializer


class TextSnippetsAPI(ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = TextSnippetsSerializer

    def get_queryset(self) -> QuerySet[TextSnippets]:
        return TextSnippets.objects.filter(created_user=self.request.user)

    def list(self, request: Request, *args, **kwargs) -> Response:
        queryset: QuerySet = self.get_queryset()
        data = {
            'total_count': queryset.count(),
            'snippets': self.serializer_class(queryset, context={'request': request}, many=True).data
        }
        return Response(data)


class TagListAPI(ListAPIView):
    queryset = Tags.objects.all()
    serializer_class = TagListSerializer


class TagRetrieveAPI(RetrieveAPIView):
    queryset = Tags.objects.all()
    serializer_class = TagDetailSerializer
