from django.contrib import admin
from .models import Task, Tag

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['name', 'color']

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ['title', 'owner', 'priority', 'status', 'due_date', 'created_at']
    list_filter = ['priority', 'status', 'tags']
    search_fields = ['title', 'owner__username']
    filter_horizontal = ['tags']