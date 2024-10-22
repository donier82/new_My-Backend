from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import About
from apps.telegram_bot.views import get_message


def about(request):
    main_page = "О нас"
    # about = About.objects.latest('id')
    about = About.objects.all()
    return render(request, 'about.html', locals())

def send_message(request):
    get_message(request, "Привет \n У вас заявка на обсуждение")
    return redirect("index")