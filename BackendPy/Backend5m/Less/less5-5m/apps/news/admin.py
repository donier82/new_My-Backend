from django.contrib import admin
from .models import News, CategoryNews

# Register your models here.
@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description')
    list_filter = ['id']
    search_fields = ('id', 'title', 'description')


@admin.register(CategoryNews)
class CategoryNewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')