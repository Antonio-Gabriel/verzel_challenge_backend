from rest_framework import permissions, viewsets

from ..models import Lesson, LessonSerializer


class LessonServiceViewSet(viewsets.ModelViewSet):
    """Lesson Service"""

    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly,
    ]
