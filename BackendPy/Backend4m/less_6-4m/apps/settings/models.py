from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class Settings(models.Model):
    title = models.CharField(
        max_length=155,
        verbose_name='Заголовка'
    )
    descriptions = models.TextField(
        verbose_name='Описание'
    )
    image1 = models.ImageField(
        upload_to='settings/',
        verbose_name='Фото 1'
    )
    image2 = models.ImageField(
        upload_to='settings/',
        verbose_name='Фото 2'
    )
    image3 = models.ImageField(
        upload_to='settings/',
        verbose_name='Фото 3'
    )
    facebook = models.URLField()
    twitter = models.URLField()
    youtube = models.URLField()
    linkedin = models.URLField()

    def __str__(self) -> str:
        return self.title
    
    class Meta:
        verbose_name_plural = 'Настройка Главной'

class Shape(models.Model):
    title = models.CharField(
        max_length=155,
        verbose_name='Заголовка'
    )
    descriptions = RichTextField(
        verbose_name='Описание'
    )
    image = models.ImageField(
        upload_to='shape',
        verbose_name='Фото'
    )

    def __str__(self) -> str:
        return self.title
    
    class Meta:
        verbose_name_plural = 'Shape'

class About(models.Model):
    image1 = models.ImageField(
        upload_to='settings/',
        verbose_name='Фото 1'
    )
    image2 = models.ImageField(
        upload_to='settings/',
        verbose_name='Фото 2'
    )
    image3 = models.ImageField(
        upload_to='settings/',
        verbose_name='Фото 3'
    )
    title = models.CharField(
        max_length=155,
        verbose_name='Заголовка'
    )
    descriptions = RichTextField(
        verbose_name='Описание'
    )

    def __str__(self) -> str:
        return self.title
    
    class Meta:
        verbose_name_plural = ' О нас'


class Contact(models.Model):
    name = models.CharField(
        max_length=155,
        verbose_name='Имя'
    )
    email = models.EmailField(
        verbose_name='Почта'
    )
    phone = models.CharField(
        max_length=50,
        verbose_name='Номер телефона'
    )
    subject = models.CharField(
        max_length=155,
        verbose_name='Обьект'
    )
    message = models.TextField(
        verbose_name='Сообщение'
    )


    def __str__(self) -> str:
        return self.name
    
    class Meta:
        verbose_name_plural = 'Отзывы'