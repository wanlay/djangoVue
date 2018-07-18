from django.urls import path
from rest_framework import routers
from rest_framework.schemas import get_schema_view

from api.users import views

schema_view = get_schema_view(title='Pastebin API')

router = routers.SimpleRouter()
router.register(r"users", views.UserViewSet)

urlpatterns = [
    path(r'', schema_view),
] + router.urls
