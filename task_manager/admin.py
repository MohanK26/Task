# task_manager/admin.py

from django.contrib import admin
from .models import UserRegistration, Task1

admin.site.register(UserRegistration)


@admin.register(Task1)
class Task1Admin(admin.ModelAdmin):
    list_display = ('title', 'due_date', 'is_completed', 'priority')
    list_filter = ('is_completed', 'priority')
    search_fields = ('title', 'description')
    ordering = ('-due_date', 'priority')
