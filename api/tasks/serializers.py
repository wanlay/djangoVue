from rest_framework import serializers
from django_celery_beat.models import CrontabSchedule, IntervalSchedule, PeriodicTask


class CrontabSerializer(serializers.ModelSerializer):
    class Meta:
        model = CrontabSchedule
        fields = '__all__'


class IntervalSerializer(serializers.ModelSerializer):
    class Meta:
        model = IntervalSchedule
        fields = '__all__'


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = PeriodicTask
        fields = '__all__'
