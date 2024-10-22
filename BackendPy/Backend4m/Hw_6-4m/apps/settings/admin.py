from django.contrib import admin
from apps.settings.models import About, Settings, Shape, Contact, RunText

# Register your models here.
admin.site.register(Settings)
admin.site.register(Shape)
admin.site.register(About)
admin.site.register(Contact)
admin.site.register(RunText)
