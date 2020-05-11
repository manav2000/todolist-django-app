from django.contrib import admin
from .models import TaskList, DoneTasks

# Register your models here.


class TodoAdmin(admin.ModelAdmin):
    list_display = ('task', 'pub_date', 'priority')


class DoneTaskAdmin(admin.ModelAdmin):
    list_display = ('completed_task', 'completion_date')


admin.site.register(TaskList, TodoAdmin)
admin.site.register(DoneTasks, DoneTaskAdmin)
