"""
todo list model
"""
from django.db import models


class TodoItem(models.Model):
    """
    Model representing a single Todo item.

    Attributes:
        task_id (int): The unique identifier for the task.
        title (str): The title or description of the task.
        stat (bool): The status of the task, whether it's completed or not.
        created_date (DateTime): The date and time when the task was created.
    """
    task_id = models.BigAutoField(primary_key=True)
    title = models.TextField(max_length=500)
    stat = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title}"
