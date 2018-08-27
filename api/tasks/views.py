from itertools import chain
from django_celery_beat.models import CrontabSchedule, IntervalSchedule, PeriodicTask
from rest_framework import viewsets, filters
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from api.tasks.serializers import CrontabSerializer, IntervalSerializer, TaskSerializer
from djangovue.celery import app
from celery import shared_task


class CrontabViewSet(viewsets.ModelViewSet):
    """
    CURD of Crontab
    """
    permission_classes = (IsAuthenticated,)
    queryset = CrontabSchedule.objects.all()
    serializer_class = CrontabSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('id', )


class IntervalViewSet(viewsets.ModelViewSet):
    """
    CURD of Interval
    """
    permission_classes = (IsAuthenticated,)
    queryset = IntervalSchedule.objects.all()
    serializer_class = IntervalSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('id', )


class TaskViewSet(viewsets.ModelViewSet):
    """
    CURD of Task
    """
    permission_classes = (IsAuthenticated,)
    queryset = PeriodicTask.objects.all()
    serializer_class = TaskSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('id', )

@shared_task
def add(x, y):
    return x + y


class TaskList(APIView):
    """
    获取任务列表
    """
    def get(self, request, *args, **kwargs):
        i = app.control.inspect().registered_tasks()
        if i :
            reg_tasks = set(chain.from_iterable(i.values()))
            # reg_tasks = list(sorted(name for name in current_app.tasks if not name.startswith('celery.')))
            return Response(reg_tasks)
        else:
            return Response("")
