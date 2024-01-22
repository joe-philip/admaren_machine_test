from django.urls import path
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView

from . import views

router = DefaultRouter()

router.register(
    'text_snippets', views.TextSnippetsAPI,
    basename='text_snippets'
)

urlpatterns = [
    path('signup', views.SignupAPI.as_view()),
    path('login', TokenObtainPairView.as_view(), name='login')
]+router.urls
