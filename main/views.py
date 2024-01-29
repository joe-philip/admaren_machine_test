from django.db.models import QuerySet
from rest_framework.exceptions import NotFound
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView
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

    def destroy(self, request: Request, *args, **kwargs) -> Response:
        self.perform_destroy(self.get_object())
        queryset = self.get_queryset()
        return Response(self.serializer_class(queryset, context=self.get_serializer_context(), many=True).data)


class TextSnippetsDeleteAPI(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request: Request) -> Response:
        from .serializers import TextSnippetsDeleteSerializer

        serializer = TextSnippetsDeleteSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        snippets = map(
            lambda x: x.id, serializer.validated_data.get('snippets', [])
        )
        queryset = TextSnippets.objects.filter(
            created_user=self.request.user,
        )
        delete_queryset, response_queryset = queryset.filter(id__in=snippets), queryset.exclude(id__in=snippets)  # noqa E501 # pylint: disable=line-too-long
        if delete_queryset.exists():
            delete_queryset.delete()
            return Response(TextSnippetsSerializer(response_queryset, context={'request': request}, many=True).data)
        raise NotFound('No snippets found')


class TagListAPI(ListAPIView):
    queryset = Tags.objects.all()
    serializer_class = TagListSerializer


class TagRetrieveAPI(RetrieveAPIView):
    queryset = Tags.objects.all()
    serializer_class = TagDetailSerializer
