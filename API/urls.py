"""
url handler for: /api
"""
from django.urls import path
from . import views

urlpatterns = [
    path("/tasks", views.TodoItemListAPIView.as_view())
]
