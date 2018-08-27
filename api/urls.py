from django.urls import path
from rest_framework import routers

from api.tasks.views import CrontabViewSet, IntervalViewSet, TaskViewSet, TaskList
from api.users.views import UserViewSet

router = routers.SimpleRouter(trailing_slash=False)
router.register(r"users", UserViewSet)
router.register(r"crontab", CrontabViewSet)
router.register(r"interval", IntervalViewSet)
router.register(r"task", TaskViewSet)

urlpatterns = [
    path(r'regtask', TaskList.as_view(), name='reg_task'),
] + router.urls
