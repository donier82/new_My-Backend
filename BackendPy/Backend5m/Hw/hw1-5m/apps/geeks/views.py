from django.shortcuts import render
from rest_framework.generics import ListAPIView, CreateAPIView , RetrieveAPIView, UpdateAPIView, DestroyAPIView

from .models import Settings
from .serializers import *


# Create your views here.
class SettingsAPIView(ListAPIView):  
    queryset = Settings.objects.all()
    serializer_class = SettingsSerializer

class SettingsCreateAPI(CreateAPIView):
    queryset = Settings.objects.all()
    serializer_class = SettingsCreateSerializer

class SettingsRetrieveAPI(RetrieveAPIView):
    queryset = Settings.objects.all()
    serializer_class = SettingsSerializer

class SettingsUpdateAPI(UpdateAPIView):
    queryset = Settings.objects.all()
    serializer_class = SettingsSerializer

class SettingsDestroyAPI(DestroyAPIView):
    queryset = Settings.objects.all()
    serializer_class = SettingsSerializer


