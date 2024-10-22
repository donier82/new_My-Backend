from django.shortcuts import render
from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet
"""
APIView
ViewSet
"""

from .models import *
from .serializers import *

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
