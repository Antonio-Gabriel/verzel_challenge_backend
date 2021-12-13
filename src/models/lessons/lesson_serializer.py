from .lessons import Lesson

from rest_framework import serializers

class LessonSerializer(serializers.ModelSerializer):
    """ Lesson Serializer """

    class Meta:
        model = Lesson
        fields = "__all__"