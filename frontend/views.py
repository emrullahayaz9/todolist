"""
Views for managing Todo items.
"""

from django.shortcuts import render
from django.http import HttpResponse
from .models import TodoItem
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.core.exceptions import ObjectDoesNotExist


def home(request):
    """
    Function to render the home page.
    Lists all tasks when a GET request is received.
    adds a new task when a POST request is received.
    """
    all_tasks = TodoItem.objects.all()
    if request.method == "GET":
        tasks = TodoItem.objects.all()
        state = True
        return render(request, "index.html", {"tasks": tasks, "state": state})

    if request.method == "POST":
        task_name = request.POST.get("task")
        if task_name:
            TodoItem.objects.create(title=task_name)
            tasks = TodoItem.objects.all()
            state = False
    return render(request, "index.html", {"tasks": all_tasks, "state": state})


@csrf_exempt
def delete(request, task_id):
    """
    Function to delete a task.
    Deletes the task with the specified id.
    """
    try:
        TodoItem.objects.filter(task_id=task_id).delete()
        state = True
        all_tasks = TodoItem.objects.all()
        return render(request, "index.html", {"tasks": all_tasks, "state": state})
    except ObjectDoesNotExist:
        return HttpResponse("CANNOT FIND THE OBJECT")


def edit(request, task_id):
    """
    Function to edit a task.
    Edits the task with the specified id.
    """
    if request.method == "POST":
        edited = request.POST.get("edited")
        task = TodoItem.objects.get(task_id=task_id)
        task.title = edited
        task.save()
        return JsonResponse(status=200)
    else:
        """
        If the user sends a request to /edit and
        it is not a POST request, then the user will not do anything.
        """
        return JsonResponse(status=401)


def checkbox(request, task_id):
    """
    Function to toggle the checkbox for a task.
    Toggles the checkbox status for the task with the specified id.
    """
    if request.method == "POST":
        task = TodoItem.objects.get(task_id=task_id)
        if task.stat is True:
            task.stat = False
            task.save()
        else:
            task.stat = True
            task.save()
    state = False
    all_tasks = TodoItem.objects.all()
    return render(request, "index.html", {"tasks": all_tasks, "state": state})
