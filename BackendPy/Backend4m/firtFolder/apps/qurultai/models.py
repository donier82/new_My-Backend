from django.db import models

# Create your models here.
class Settings(models.Model):
    logo = models.ImageField(upload_to="logo_image/")
    title = models.CharField(max_length=155, verbose_name="Заголовок")
    water_mark = models.CharField(max_length=155, verbose_name="Водяной знак на баннере")
    banner = models.ImageField(upload_to="banner_image/")

    def __str__(self) -> str:
        return "Настройки сайта"
    
    class Meta:
        verbose_name = ""
        verbose_name_plural = "Основные настройки сайта"