from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm


def index(request):
    tasks = Task.objects.all()
    form = TaskForm()
    context = {'tasks': tasks, 'form': form}

    if request.method == 'POST':
        item = None
        form = TaskForm(request.POST)
        update = form.data.get('update')
        delete = form.data.get('delete')
        pk = form.data.get('pk')

        if pk:
            try:
                pk = int(pk)
                item = Task.objects.filter(id=pk).first()
            except ValueError:
                pass

        if update and item:
            form.instance = item
            form.save()
            return redirect('list')

        if delete and item:
            item.delete()
            return redirect('list')

        if form.is_valid():
            form.save()
        return redirect('list')

    return render(request, 'index.html', context)
