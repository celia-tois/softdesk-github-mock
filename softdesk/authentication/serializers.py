from rest_framework.serializers import ModelSerializer
from authentication.models import User
from django.contrib.auth.hashers import make_password


class SignupSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'password')

    def validate_password(self, value: str) -> str:
        """
        Hash value passed by user.

        :param value: password of a user
        :return: a hashed version of the password
        """
        return make_password(value)
