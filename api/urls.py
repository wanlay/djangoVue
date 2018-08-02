from django.urls import path
from rest_framework import routers

from api.tasks.views import CrontabViewSet, IntervalViewSet, TaskViewSet
from api.users.views import UserViewSet

router = routers.SimpleRouter()
router.register(r"users", UserViewSet)
router.register(r"crontab", CrontabViewSet)
router.register(r"interval", IntervalViewSet)
router.register(r"task", TaskViewSet)

urlpatterns = router.urls
