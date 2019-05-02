from .models import Task
from django.utils import timezone
from django.shortcuts import render, get_object_or_404
from .forms import TaskForm
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required

# def task_list(request):
#     return HttpResponse('ok')

# Create your views here.


def task_list(request):
    if request.user.is_authenticated:
        tasks = Task.objects.filter(user=request.user, created_date__lte=timezone.now()).order_by('_date')
    else:
        tasks = []
    return render(request, 'todo_list/task_list.html', {'tasks': tasks})


def task_detail(request, pk):
    task = get_object_or_404(Task, pk=pk)
    return render(request, 'todo_list/task_detail.html', {'task': task})


@login_required
def task_new(request):
    if request.method == "POST":
        print(request)
        print(request.POST)
        form = TaskForm(request.POST)
        if form.is_valid():
            print('valid')
            task = form.save(commit=False)
            task.user = request.user
            task.save()
            return redirect('task_detail', pk=task.pk)
    else:
        form = TaskForm()
    return render(request, 'todo_list/task_edit.html',
                  {'form': form, 'command': 'New'})


@login_required
def task_edit(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            task = form.save(commit=False)
            task.save()
            return redirect('task_detail', pk=task.pk)
    else:
        form = TaskForm(instance=task)
    return render(request, 'todo_list/task_edit.html',
                  {'form': form, 'command': 'Edit'})


@login_required
def task_delete(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.delete()
    return redirect('task_list')


@login_required
def task_complete(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.complete()
    return redirect('task_list')
