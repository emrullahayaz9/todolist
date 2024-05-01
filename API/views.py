"""
api view
"""
from rest_framework import generics
from frontend.models import TodoItem
from .serializers import TodoSerializer
class TodoItemListAPIView(generics.ListAPIView):
    queryset = TodoItem.objects.all()
    serializer_class = TodoSerializer