from rest_framework import serializers

from .models import Settings

class SettingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Settings
        fields = '__all__'
        # fields = ['id', 'title', 'description']

class SettingsCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Settings
        fields = ('title', 'description')

class SettingsUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Settings
        fields = ('description',)