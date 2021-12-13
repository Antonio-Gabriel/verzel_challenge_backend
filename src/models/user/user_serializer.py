from .user import User

from rest_framework import serializers
from django.contrib.auth.hashers import make_password


class UserSerializer(serializers.ModelSerializer):
    """User serializer"""

    password = serializers.CharField(
        style={"input_type": "password"}, write_only=True, label="Password"
    )

    class Meta:
        extra_kwargs = {"email": {"write_only": True}, "password": {"write_only": True}}
        model = User
        fields = ("id", "username", "password", "state", "created_at", "updated_at")

    validate_password = make_password

    def validate_password(self, value):
        if len(value) > 6:
            return value

        return serializers.ValidationError(
            "A palavra passe precisa conter no mínimo 6 caracteres"
        )
