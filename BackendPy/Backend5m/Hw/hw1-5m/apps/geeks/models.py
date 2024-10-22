from django.db import models
#from django.db.models import Model

# Create your models here.
class Settings(models.Model):
    title= models.CharField(max_length=155, verbose_name='Заголовок')
    description=models.TextField(verbose_name='Описание', default='по-умолчанию')
def __str__(self):
    return self.title

class Meta:
    verbose_name=''
    verbose_name_plural='Основные настройки'