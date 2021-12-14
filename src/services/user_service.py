from ..models import User, UserSerializer
from ..helper import generate_access_token

from rest_framework import status
from rest_framework import mixins, viewsets

# from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.generics import GenericAPIView


from django.contrib.auth.models import User as UserModel


class UserServiceViewSet(
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    mixins.ListModelMixin,
    viewsets.GenericViewSet,
):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserLoginAPIView(GenericAPIView):
    permission_classes = (AllowAny,)

    def post(self, request):
        email = request.data.get("email", None)
        user_password = request.data.get("password", None)

        if not user_password:
            raise AuthenticationFailed("A user password is needed.")

        if not email:
            raise AuthenticationFailed("An user email is needed.")

        user_instance = User.objects.get(email=email, password=user_password)

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

            if not user_model.username:
                user_model.save()
            else:
                response.data = {"access_token": user_access_token}

            response.data = {"access_token": user_access_token}

            return response

        return Response(
            {"message": "Something went wrong."}, status=status.HTTP_401_UNAUTHORIZED
        )
