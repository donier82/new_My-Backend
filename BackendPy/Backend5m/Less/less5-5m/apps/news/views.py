from django.shortcuts import render
from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet
from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated, IsAuthenticatedOrReadOnly

"""
APIView
ViewSet
"""

from .models import *
from .serializers import *
from .permissions import *

# Create your views here.
class NewsAPI(GenericViewSet,
              mixins.ListModelMixin,
              mixins.CreateModelMixin,
              mixins.RetrieveModelMixin,
              mixins.UpdateModelMixin,
              mixins.DestroyModelMixin,
              ):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    permission_classes = (IsAdminUserOrReadOnly, )

"""
AllowAny - полный доступ
IsAdminUser - дает доступ только админу
IsAuthenticated - авторизованные пользователи
IsAuthenticatedOrReadOnly - авторизованные пользователи могут выполнять все действия
а не авторизованные только просмотреть (то есть method GET)
"""