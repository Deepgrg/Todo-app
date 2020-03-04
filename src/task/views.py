from django.shortcuts import render, redirect

from .models import *
from .forms import TaskForm

def indexPage(request):
    tasks = Task.objects.all();
    context= {
        'tasks': tasks,
    }
    return render(request , "task/indexPage.html", context)


def addTask(request):
    task_form = TaskForm()
    if request.method =="POST" :
        task_form=TaskForm(request.POST)
        if task_form.is_valid():
            task_form.save()
            return redirect('index_page')
    context={
        'form': task_form,
    }
    return render(request, "task/addTask.html" , context)

def updateTask(request , pk):
    task_detail = Task.objects.get(id = pk)
    task_form= TaskForm(instance= task_detail)

    if request.method== "POST":
        task_form = TaskForm(request.POST , instance=task_detail)
        if task_form.is_valid():
            task_form.save()
            return redirect('index_page')

    context={
        'form':task_form,
    }
    return render(request,"task/updateTask.html", context)

def deleteTask(request , pk):
    task_detail = Task.objects.get(id=pk)
    if request.method =="POST":
        task_detail.delete()
        return redirect('index_page')
    context ={
        'task': task_detail,
    }
    return render(request , 'task/deleteTask.html' , context)