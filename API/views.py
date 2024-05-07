"""
API view for listing Todo items.
"""
from rest_framework import generics
from frontend.models import TodoItem
from .serializers import TodoSerializer


class TodoItemListAPIView(generics.ListAPIView):
    """
    API view to list all Todo items.
    """
    queryset = TodoItem.objects.all()
    serializer_class = TodoSerializer
