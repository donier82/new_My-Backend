from django.contrib import admin
from .models import Settings

# Register your models here.
@admin.register(Settings)
class SettingsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description')
    list_filter = ['id']
    search_fields = ('id', 'title', 'description')