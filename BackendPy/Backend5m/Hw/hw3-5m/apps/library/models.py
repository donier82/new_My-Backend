
from django.db import models

# Create your models here.
class Author(models.Model):
   
    name = models.CharField(max_length=155, verbose_name="Имя")
    birthdate = models.DateField(verbose_name='дата рождение')
    

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        verbose_name=""
        verbose_name_plural="Автор"

class Book(models.Model):
   
    title = models.CharField(max_length=155, verbose_name="Книга")
    publication_year = models.DateField(verbose_name='год издание')
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')    #(on_delete=models.SET_NULL, null=True -останется по умолчанию. CASCADE-удаляет)

    def __str__(self) -> str:
        return self.title
    
    class Meta:
        verbose_name=""
        verbose_name_plural="Книга"

class Genre(models.Model):
   
    name = models.CharField(max_length=155, verbose_name="Жанр")
    birthdate = models.DateField(verbose_name='год издание')
    books = models.ManyToManyField(Book, null=True, blank=True, related_name='genre')

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        verbose_name=""
        verbose_name_plural="Жанр"