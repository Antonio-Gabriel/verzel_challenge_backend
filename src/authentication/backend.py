import jwt

from rest_framework import authentication, exceptions

from django.contrib.auth.models import User as UserModel


class JWTAuthentication(authentication.BaseAuthentication):
    def authenticate(self, request):

        auth_data = authentication.get_authorization_header(request)

        if not auth_data:
            return None

        try:
            payload = jwt.decode(
                auth_data.decode().split(" ")[1], "secret_key", algorithms="HS256"
            )
            user = UserModel.objects.get(username=payload["username"])

            return (user, auth_data.decode().split(" ")[1])

        except jwt.DecodeError:
            raise exceptions.AuthenticationFailed("Your token is invalid, login")

        except jwt.ExpiredSignatureError:
            raise exceptions.AuthenticationFailed("Your token is expired, login")

        return super().authenticate(request)
