from .models import Task
from django.utils import timezone
from django.shortcuts import render, get_object_or_404
from .forms import TaskForm
from django.shortcuts import redirect


# def task_list(request):
#     return HttpResponse('ok')

# Create your views here.


def task_list(request):
    tasks = Task.objects.filter(created_date__lte=timezone.now()).order_by
    ('_date')
    return render(request, 'todo_list/task_list.html', {'tasks': tasks})


def task_detail(request, pk):
    task = get_object_or_404(Task, pk=pk)
    return render(request, 'todo_list/task_detail.html', {'task': task})


def task_new(request):
    if request.method == "POST":
        print(request)
        print(request.POST)
        form = TaskForm(request.POST)
        if form.is_valid():
            print('valid')
            task = form.save(commit=False)
            task.save()
            return redirect('todo_list/task_detail', pk=task.pk)
    else:
        form = TaskForm()
    return render(request, 'todo_list/task_edit.html', {'form': form})


def task_edit(request, pk):
    post = get_object_or_404(Task, pk=pk)
    if request.method == "POST":
        form = TaskForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('task_detail', pk=form.pk)
    else:
        form = TaskForm(instance=form)
    return render(request, 'todo_list/task_edit.html', {'form': form})
