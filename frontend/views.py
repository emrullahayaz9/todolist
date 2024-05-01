from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import TodoItem
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse

#home page
def home(request):
    allTask = TodoItem.objects.all()
    if request.method == "GET":
        tasks = TodoItem.objects.all()
        state = True
        return render(request, "index.html", {"tasks": tasks,"state":state})

    if request.method == "POST":
        task_name = request.POST.get('task')
        if task_name:
            TodoItem.objects.create(title=task_name)
            tasks = TodoItem.objects.all()
            state = False
    return render(request, "index.html", {"tasks": allTask, "state":state})

#for deleting
@csrf_exempt
def delete(request, id):
    try:
        TodoItem.objects.filter(task_id=id).delete()
        state = True
        allTasks = TodoItem.objects.all()
        return render(request, "index.html", {"tasks": allTasks, "state":state})
    except:
        return HttpResponse("CANNOT FIND THE OBJECT")

# for editing
def edit(request, id):
    if request.method=="POST":
        edited = request.POST.get("edited")
        task = TodoItem.objects.get(task_id=id)
        task.title = edited
        task.save()
        return JsonResponse(status=200)

# for checkbox
def checkbox(request, id):
    if request.method == "POST":
        task = TodoItem.objects.get(task_id=id)
        if task.stat == True:
            task.stat = False
            task.save()          
        else:
            task.stat = True
            print(task.stat)
            task.save()
    state = False
    allTasks = TodoItem.objects.all()
    return render(request, "index.html", {"tasks": allTasks, "state":state})