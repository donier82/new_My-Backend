from django.db import models
from apps.users.models import User

# Create your models here.
class CategoryNews(models.Model):
    title = models.CharField(max_length=155, verbose_name="Категория для новостей")
    
    
    def __str__(self) -> str:
        return self.title
    
    class Meta:
        verbose_name=""
        verbose_name_plural="Категории для новостей"

class News(models.Model):
    category = models.ManyToManyField(CategoryNews,  null=True, blank=True, related_name="category_news")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_news")
    image = models.ImageField(upload_to="news_images/", null=True, blank=True)
    title = models.CharField(max_length=155, verbose_name="Заголовок")
    description = models.TextField(verbose_name="Описание", default="Описание")

    def __str__(self) -> str:
        return self.title
    
    class Meta:
        verbose_name=""
        verbose_name_plural="Новости"