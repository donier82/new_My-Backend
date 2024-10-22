from django.shortcuts import render
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView

from .models import Settings
from .serializers import *

# Create your views here.
class SettingsCreateAPI(CreateAPIView):
    queryset = Settings.objects.all()
    serializer_class = SettingsCreateSerializer

class SettingsAPIView(ListCreateAPIView):
    # "queryset - передача объектов"
    queryset = Settings.objects.all()
    serializer_class = SettingsSerializer

class SettingsRetrieveAPI(RetrieveAPIView):
    queryset = Settings.objects.all()
    serializer_class = SettingsSerializer

class SettingsUpdateAPI(UpdateAPIView):
    queryset = Settings.objects.all()
    serializer_class = SettingsSerializer

class SettingsDestroyAPI(DestroyAPIView):
    queryset = Settings.objects.all()
    serializer_class = SettingsSerializer