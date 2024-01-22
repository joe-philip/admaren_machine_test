from rest_framework.generics import CreateAPIView

from .serializers import UserSignupSerializer

# Create your views here.


class SignupAPI(CreateAPIView):
    serializer_class = UserSignupSerializer
