from django.contrib import admin
from .models import Settings

# Register your models here.
@admin.register(Settings)
class SettingAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'description']
    

