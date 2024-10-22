from django.utils import timezone
from django.db import models


class Task(models.Model):
  
    title = models.CharField(max_length=155, verbose_name="Заголовок")
    description = models.TextField(verbose_name="Описание")
    complated = models.BooleanField(default=False)    
    created = models.DateTimeField(verbose_name='Время создания: ', default=timezone.now)


    def __str__(self) -> str:
        return self.title
    
    class Meta:
        verbose_name=""
        verbose_name_plural="Задача"

