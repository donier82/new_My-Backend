from django.urls import path

from apps.settings.views import index
from apps.tg_bot.views import get_message

urlpatterns = [
    path('', index, name='index'),
    path('send_message/', get_message, name='send_message' ),
]
