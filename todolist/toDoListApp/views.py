import datetime

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers

from .models import TaskList, DoneTasks


# Create your views here.


def index(request):
    listItems = TaskList.objects.all().order_by('-pub_date')
    # shows all the completed tasks for previous 2 days
    d = datetime.date.today()-datetime.timedelta(days=2)
    tasks = DoneTasks.objects.filter(completion_date__gte=d)
    context = {
        'listItems': listItems,
        'completed_tasks': tasks
    }
    return render(request, 'toDoListApp/index.html', context)


@csrf_exempt
def add_task(request):
    current_date = timezone.now()
    content = request.POST['content']
    task_obj = TaskList.objects.create(task=content, pub_date=current_date)
    return HttpResponseRedirect('/')


# When task is done input that donetask in DoneTasks data
@csrf_exempt
def done_task(request, item_id):
    done = TaskList.objects.get(id=item_id)
    year = datetime.datetime.now().year
    month = datetime.datetime.now().month
    day = datetime.datetime.now().day
    DoneTasks.objects.create(
        completed_task=done, completion_date=datetime.date(year, month, day))

    TaskList.objects.get(id=item_id).delete()
    return HttpResponseRedirect('/')


# Delete a task
@csrf_exempt
def delete_task(request, item_id):
    TaskList.objects.get(id=item_id).delete()
    return HttpResponseRedirect('/')


# Data for use in javascript
def send_json(request):
    data = serializers.serialize('json', DoneTasks.objects.all())
    return HttpResponse(data, content_type='application/json')
