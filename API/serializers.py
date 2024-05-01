"""
for api endpoint: /api/tasks
"""
from rest_framework import serializers
from frontend.models import TodoItem

class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TodoItem
        fields = "__all__"