from django.contrib.auth import authenticate, login, logout
from rest_framework.authtoken.models import Token
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST
from rest_framework.views import APIView


class Login(APIView):
    permission_classes = (AllowAny,)
    def post(self, request, format=None):
        username = request.data.get("username", "")
        password = request.data.get("password", "")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            token, created = Token.objects.get_or_create(user=user)
            if user.is_active:
                login(request, user)
                return Response({
                    "data": {
                        "token": "TOKEN " + token.key
                    }
                })
            return Response("账号被封停", HTTP_400_BAD_REQUEST)
        return Response("用户名或者密码错误", HTTP_400_BAD_REQUEST)

class Info(APIView):
    def get(self, request, format=None):
        user = request.user
        if user.is_staff:
            role = "admin"
        else:
            role = "user"
        return Response({
            "data": {
                "roles": role,
                "name": user.username,
                "avatar": "static/img/1.gif"
            }
        }, )

class Logout(APIView):
    def post(self, request, format=None):
        logout(request)
        return Response({
            "data": {
                "message": "success"
            }
        })