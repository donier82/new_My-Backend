from django.shortcuts import render
from apps.base.models import About
from .models import Settings

# Create your views here.
def index(request):
    about = About.objects.latest('id')
    settings = Settings.objects.latest('id')
    return render(request, 'index.html', locals())

