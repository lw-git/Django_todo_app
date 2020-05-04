from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm


def index(request):
    tasks = Task.objects.all()

    form = TaskForm()

    context = {'tasks': tasks, 'form': form}

    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('list')

    return render(request, 'index.html', context)


def updateTask(request, pk):
    task = Task.objects.get(id=pk)

    form = TaskForm(instance=task)

    context = {'form': form}

    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
        return redirect('list')

    return render(request, 'update_task.html', context)


def deleteTask(request, pk):
    item = Task.objects.get(id=pk)

    context = {'item': item}

    if request.method == 'POST':
        item.delete()
        return redirect('list')

    return render(request, 'delete_task.html', context)
