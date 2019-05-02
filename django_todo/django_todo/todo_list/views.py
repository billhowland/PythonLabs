from .models import Task
from django.shortcuts import render, get_object_or_404
from .forms import TaskForm
from django.shortcuts import redirect
from django.http import HttpResponseForbidden
from django.contrib.auth.decorators import login_required

# def task_list(request):
#     return HttpResponse('ok')

# Custom decorator


def login_test(func):
    def check_and_call(request, *args, **kwargs):
        # user = request.user
        # print user.id
        pk = kwargs["pk"]
        task = Task.objects.get(pk=pk)
        if (task.user != request.user):
            return HttpResponseForbidden()
        return func(request, *args, **kwargs)
    return check_and_call


# Create your views here.


def task_list(request):
    if request.user.is_authenticated:
        tasks = Task.objects.filter(user=request.user).order_by('created_date')
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


@login_test
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


@login_test
def task_delete(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.delete()
    return redirect('task_list')


@login_test
def task_complete(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.complete()
    return redirect('task_list')
