from ..models import User as UserAdmin, UserSerializer
from ..helper import generate_access_token

from rest_framework import status
from rest_framework import mixins, viewsets

# from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.generics import GenericAPIView


from django.contrib.auth.models import User as UserModel

# from django.shortcuts import get_object_or_404


class UserServiceViewSet(
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    mixins.ListModelMixin,
    viewsets.GenericViewSet,
):
    queryset = UserAdmin.objects.all()
    serializer_class = UserSerializer


class UserLoginAPIView(GenericAPIView):
    permission_classes = (AllowAny,)

    def post(self, request):
        email = request.data.get("email", None)
        user_password = request.data.get("password", None)

        if not user_password:
            raise AuthenticationFailed("Palavra passe é obrigatório.")

        if not email:
            raise AuthenticationFailed("Email é obrigatório.")

        try:

            user_instance = UserAdmin.objects.get(email=email, password=user_password)

            if user_instance:

                serializer = UserSerializer(user_instance)

                user_model = UserModel()
                user_model.username = serializer.data["username"]

                user_access_token = generate_access_token(serializer.data["username"])

                response = Response()
                response.status_code = status.HTTP_200_OK
                response.set_cookie(
                    key="access_token", value=user_access_token, httponly=True
                )

                user_data = serializer.data

                del user_data["created_at"]
                del user_data["updated_at"]

                if not UserModel.objects.filter(
                    username__exact=serializer.data["username"]
                ):
                    user_model.save()

                else:
                    response.data = {
                        "access_token": user_access_token,
                        "user": user_data,
                    }

                response.data = {
                    "access_token": user_access_token,
                    "user": user_data,
                }

            return response

        except UserAdmin.DoesNotExist:

            user_instance = None

        return Response(
            {"message": "Algo deu errado!."}, status=status.HTTP_401_UNAUTHORIZED
        )
