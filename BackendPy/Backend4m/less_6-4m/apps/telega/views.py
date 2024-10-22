from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.conf import settings
from telebot import TeleBot, types
from .models import TelegramUser

# Create your views here.
TELEGRAM_TOKEN = "7515995824:AAELxZtsL0mqCab4cRWC5U1dlIOTfatwxkQ"
# ADMIN_ID = 1904375259

bot = TeleBot(TELEGRAM_TOKEN, threaded=False)
admins = TelegramUser.objects.filter(is_admin = True)
print(admins)


@bot.message_handler(commands=['start'])
def start(message:types.Message):
    TelegramUser.objects.get_or_create(username = message.from_user.username, id_user=message.from_user.id, first_name = message.from_user.first_name, last_name = message.from_user.last_name, chat_id=message.chat.id)
    # bot.delete_message(message.chat.id, message.message_id) 
    bot.send_message(message.chat.id, f"Привет {message.from_user.full_name}")


def get_message(text):
    for admin in admins:
        bot.send_message(admin.chat_id, text)


@bot.message_handler()  
def echo(message:types.Message):
    # bot.delete_message(message.chat.id, message.message_id)  
    bot.send_message(message.chat.id, "Я вас не понял")