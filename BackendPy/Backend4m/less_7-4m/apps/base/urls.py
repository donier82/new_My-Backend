from django.urls import path

from apps.base.views import about, send_message

urlpatterns = [
    # path('', index, name="index"),
    path('about/', about, name="about"),
    path('send_message/', send_message, name="send_message"),
]