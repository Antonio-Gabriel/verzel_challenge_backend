from .module import Module

from rest_framework import serializers


class ModuleSerializer(serializers.ModelSerializer):
    """Module Serializer"""

    # HyperLinked Related Field
    lessons = serializers.HyperlinkedRelatedField(
        many=True, read_only=True, view_name="lesson-detail"
    )

    class Meta:
        model = Module
        fields = ("id", "name", "lessons")
