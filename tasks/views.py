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
    return render(request, "tasks/details.html", {"task" : task})

def finish(requst, pk):
    task = get_object_or_404(Todo_task, pk=pk)
    if task != Http404: 
        task.task_finished = True
        task.task_finished_date = timezone.now()
        task.save()
    return HttpResponseRedirect(reverse("tasks:index"))
