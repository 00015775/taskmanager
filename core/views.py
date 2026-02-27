from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from tasks.models import Task


@login_required
def dashboard_view(request):
    user_tasks = Task.objects.filter(owner=request.user)

    context = {
        'total': user_tasks.count(),
        'todo': user_tasks.filter(status='todo').count(),
        'in_progress': user_tasks.filter(status='in_progress').count(),
        'done': user_tasks.filter(status='done').count(),
        'high_priority': user_tasks.filter(priority='high', status__in=['todo', 'in_progress']),
        'recent_tasks': user_tasks[:5],
    }
    return render(request, 'core/dashboard.html', context)
