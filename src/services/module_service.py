from rest_framework import viewsets
from rest_framework import permissions

from ..models import Module, ModuleSerializer


class ModuleServiceViewSet(viewsets.ModelViewSet):
    """Module Service"""

    queryset = Module.objects.all()
    serializer_class = ModuleSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly,
    ]
