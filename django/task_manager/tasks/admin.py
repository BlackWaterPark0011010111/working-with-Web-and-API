from django.contrib import admin
from .models import Task

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'priority', 'assigned_to', 'due_date', 'created_at', 'updated_at')
    search_fields = ('title', 'description')