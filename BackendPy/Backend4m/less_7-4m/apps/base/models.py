from django.db import models

# Create your models here.
class About(models.Model):
    image = models.ImageField(
        upload_to="about_images/",
        verbose_name="Фотография",
        null=True, blank=True,
    )
    title = models.CharField(
        max_length=200,
        verbose_name="Заголовок"
    )
    description = models.TextField(
        verbose_name="Описание"
    )

    def __str__(self):
        return f"{self.id}) - {self.title}"
    
    class Meta:
        verbose_name="О нас"
        verbose_name_plural="О нас"

"""
test = About()
print(test) # {self.id}) - {self.title}
print(test.title) # self.title


"""

"""
cursor.execute(
CREATE TABLE IF NOT EXISTS about(
title VARCHAR (200),
description TEXT
)
)

"""