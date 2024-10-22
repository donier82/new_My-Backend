from django.contrib import admin
from apps.settings.models import About, Settings, Shape, Contact

# Register your models here.
admin.site.register(Settings)
admin.site.register(Shape)
admin.site.register(About)
admin.site.register(Contact)
