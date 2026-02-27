from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Task, Tag
from .forms import TaskForm, TagForm


@login_required
def task_list_view(request):
    tasks = Task.objects.filter(owner=request.user)

    # Filtering
    status_filter = request.GET.get('status')
    priority_filter = request.GET.get('priority')
    tag_filter = request.GET.get('tag')

    if status_filter:
        tasks = tasks.filter(status=status_filter)
    if priority_filter:
        tasks = tasks.filter(priority=priority_filter)
    if tag_filter:
        tasks = tasks.filter(tags__id=tag_filter)

    tags = Tag.objects.all()

    context = {
        'tasks': tasks,
        'tags': tags,
        'status_filter': status_filter,
        'priority_filter': priority_filter,
        'tag_filter': tag_filter,
    }
    return render(request, 'tasks/task_list.html', context)


@login_required
def task_create_view(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.owner = request.user
            task.save()
            form.save_m2m()  # save many-to-many (tags)
            messages.success(request, f'Task "{task.title}" created successfully.')
            return redirect('task_list')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = TaskForm()

    return render(request, 'tasks/task_form.html', {'form': form, 'action': 'Create'})


@login_required
def task_detail_view(request, pk):
    task = get_object_or_404(Task, pk=pk, owner=request.user)
    return render(request, 'tasks/task_detail.html', {'task': task})


@login_required
def task_edit_view(request, pk):
    task = get_object_or_404(Task, pk=pk, owner=request.user)

    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            messages.success(request, f'Task "{task.title}" updated successfully.')
            return redirect('task_detail', pk=pk)
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = TaskForm(instance=task)

    return render(request, 'tasks/task_form.html', {'form': form, 'action': 'Edit', 'task': task})


@login_required
def task_delete_view(request, pk):
    task = get_object_or_404(Task, pk=pk, owner=request.user)

    if request.method == 'POST':
        title = task.title
        task.delete()
        messages.success(request, f'Task "{title}" deleted successfully.')
        return redirect('task_list')

    return render(request, 'tasks/task_confirm_delete.html', {'task': task})


@login_required
def tag_list_view(request):
    if request.method == 'POST':
        form = TagForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Tag created successfully.')
            return redirect('tag_list')
    else:
        form = TagForm()

    tags = Tag.objects.all()
    return render(request, 'tasks/tag_list.html', {'tags': tags, 'form': form})
