from django.contrib import admin
from .models import Task, Tag


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['name', 'color', 'task_count']
    search_fields = ['name']

    def task_count(self, obj):
        return obj.tasks.count()
    task_count.short_description = 'Tasks Using Tag'


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ['title', 'owner', 'priority', 'status', 'due_date', 'created_at']
    list_filter = ['priority', 'status', 'tags']
    search_fields = ['title', 'owner__username', 'description']
    filter_horizontal = ['tags']
    readonly_fields = ['created_at', 'updated_at']
    list_editable = ['status', 'priority']

    fieldsets = (
        ('Task Info', {
            'fields': ('title', 'description', 'owner')
        }),
        ('Status & Priority', {
            'fields': ('status', 'priority', 'due_date')
        }),
        ('Tags', {
            'fields': ('tags',)
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )