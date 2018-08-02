from django_celery_beat.models import CrontabSchedule, IntervalSchedule, PeriodicTask
from rest_framework import viewsets, filters
from rest_framework.permissions import IsAuthenticated

from api.tasks.serializers import CrontabSerializer, IntervalSerializer, TaskSerializer


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

