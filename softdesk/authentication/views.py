from rest_framework import generics
from authentication.serializers import SignupSerializer


class SignupUserViewset(generics.CreateAPIView):
    serializer_class = SignupSerializer
