from django.contrib import admin
from .models import Author, Book, Genre

# Register your models here.
@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'birthdate')
    # list_filter = ['id']
    # search_fields = ('id', 'title', 'description')

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'publication_year')
    # list_filter = ['id']
    # search_fields = ('id', 'title', 'description')

@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    # list_filter = ['id']
    # search_fields = ('id', 'title', 'description')