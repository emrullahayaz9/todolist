"""
serializer for api endpoint: /api/tasks
"""
from rest_framework import serializers
from frontend.models import TodoItem


class TodoSerializer(serializers.ModelSerializer):
    """
    Serializer for TodoItem model.
    """
    class Meta:
        """
        Meta class to define serializer metadata.
        """
        model = TodoItem
        fields = "__all__"
