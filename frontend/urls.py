"""
for main url controller: /
"""
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('edit/<int:task_id>/', views.edit, name="edit"),
    path('delete/<int:task_id>/', views.delete, name="delete"),
    path('checkbox/<int:task_id>/', views.checkbox, name="checkbox"),
]
