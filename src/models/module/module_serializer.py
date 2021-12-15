from .module import Module

from rest_framework import serializers

from ..lessons.lesson_serializer import LessonSerializer


class ModuleSerializer(serializers.ModelSerializer):
    """Module Serializer"""

    # HyperLinked Related Field
    # lessons = serializers.HyperlinkedRelatedField(
    #     many=True, read_only=True, view_name="lesson-detail"
    # )

    lessons = LessonSerializer(many=True, read_only=True)

    class Meta:
        model = Module
        fields = ("id", "name", "lessons")
