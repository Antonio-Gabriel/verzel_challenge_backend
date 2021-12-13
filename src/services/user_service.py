from rest_framework import mixins, viewsets

from ..models import User, UserSerializer


class UserServiceViewSet(    
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,    
    mixins.ListModelMixin,
    viewsets.GenericViewSet
):
    queryset = User.objects.all()
    serializer_class = UserSerializer
