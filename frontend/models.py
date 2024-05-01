"""
todo list model
"""
from django.db import models

class TodoItem(models.Model):
    task_id = models.BigAutoField(primary_key=True)
    title = models.TextField(max_length=500)
    stat = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.title}"