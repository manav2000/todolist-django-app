from django.db import models

# Create your models here.

# Data for tasks to be done


class TaskList(models.Model):
    task = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date_published')

    def __str__(self):
        return self.task

# Data for completed tasks


class DoneTasks(models.Model):
    completed_task = models.CharField(max_length=200)
    completion_date = models.DateTimeField('date_of_completion')

    def __str__(self):
        return self.completed_task
