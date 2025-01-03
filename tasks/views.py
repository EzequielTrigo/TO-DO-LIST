from django.shortcuts import render, get_object_or_404
from .models import Todo_task
from django.utils import timezone
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.urls import reverse

def index(request):
    some_near_date_task = Todo_task.objects.filter(task_finished=False).filter(task_start_date__lte = timezone.now()).order_by("-task_expected_finish_date")[:5]
    context = {
        "latest_task_list" : some_near_date_task,
        }
    return render(request,"tasks/index.html",context)

def details(request, pk):
    task = get_object_or_404(Todo_task ,pk=pk)
    if task.task_finished:
        is_overtime = task.task_finished_date > task.task_expected_finish_date
        overtime = task.task_finished_date - task.task_expected_finish_date
    else:
        is_overtime = task.task_expected_finish_date < timezone.now()
        overtime = timezone.now()-task.task_expected_finish_date
    return render(request, "tasks/details.html", {"task" : task,"overtime" : overtime, "is_overtime" : is_overtime })

def finish(requst, pk):
    task = get_object_or_404(Todo_task, pk=pk)
    if task != Http404: 
        task.task_finished = True
        task.task_finished_date = timezone.now()
        task.save()
    return HttpResponseRedirect(reverse("tasks:index"))

def createTask(request):
    return render(request,"tasks/create.html")

def createConfirmation(request):
    task_comments_a = request.POST['comentarios']
    print(task_comments_a)
    task_start_date_a = request.POST["task_start_date"]
    task_expected_finish_date_a = request.POST["task_expected_finish_date"]
    task_name_a = request.POST["task_name"]
    
    task=Todo_task.objects.create(task_name=task_name_a, task_comments=task_comments_a,
                                  task_start_date=task_start_date_a, task_expected_finish_date = task_expected_finish_date_a)
    print(task.task_comments)
    return HttpResponseRedirect(reverse("tasks:index"))