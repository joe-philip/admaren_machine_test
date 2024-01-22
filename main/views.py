from django.db.models import QuerySet
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from .models import TextSnippets
from .serializers import TextSnippetsSerializer, UserSignupSerializer

# Create your views here.


class SignupAPI(CreateAPIView):
    serializer_class = UserSignupSerializer


class TextSnippetsAPI(ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = TextSnippetsSerializer

    def get_queryset(self) -> QuerySet[TextSnippets]:
        return TextSnippets.objects.filter(created_user=self.request.user)
