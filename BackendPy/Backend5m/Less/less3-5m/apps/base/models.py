from django.db import models

# Create your models here.
class Settings(models.Model):
    title = models.CharField(max_length=155, verbose_name="Заголовок")
    description = models.TextField(verbose_name="Описание", default="Описание")

    def __str__(self) -> str:
        return self.title
    
    class Meta:
        verbose_name=""
        verbose_name_plural="Основные настройки"