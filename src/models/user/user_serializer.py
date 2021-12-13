from .user import User

from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    """User serializer"""

    class Meta:
        extra_kwargs = {"email": {"write_only": True}}
        model = User
        fields = "__all__"

    def validate_password(self, value):
        if len(value) > 6:
            return value

        return serializers.ValidationError(
            "A palavra passe precisa conter no mínimo 6 caracteres"
        )
