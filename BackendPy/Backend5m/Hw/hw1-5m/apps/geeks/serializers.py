from rest_framework import serializers
from .models import Settings

class SettingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Settings
        fields = ['id', 'title', 'description']

class SettingsCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Settings
        fields = ['id', 'title']

class SettingsUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Settings
        fields = ('description',)

class SettingsDestroySerializer(serializers.ModelSerializer):
    class Meta:
        model = Settings
        fields = ('id',)

