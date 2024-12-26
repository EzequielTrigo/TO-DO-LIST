from django.contrib import admin
from .models import Todo_task
# Register your models here.
class TaskAdmin(admin.ModelAdmin):
    fieldsets = [(None, {"fields": ["task_name"]}),
                 ("Comments", {"fields": ["task_comments"]}),
                 ("Date infomation", {"fields": ["task_start_date", "task_expected_finish_date"]}),
                 ("Task finish info", {"fields": ["task_finished", "task_finished_date"]}),
                 
                 ]

admin.site.register(Todo_task, TaskAdmin)