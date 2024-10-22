from django.shortcuts import render
from django.conf import settings
from telebot import TeleBot, types
from .models import TelegramUser

# Create your views here.
TELEGRAM_TOKEN = "7515995824:AAELxZtsL0mqCab4cRWC5U1dlIOTfatwxkQ"
# ADMIN_ID = 1904375259

bot = TeleBot(TELEGRAM_TOKEN, threaded=False)
admins = TelegramUser.objects.filter(is_admin = True)
#print(admins)


@bot.message_handler(commands=['start'])
def start(message:types.Message):
    TelegramUser.objects.get_or_create(username = message.from_user.username, id_user=message.from_user.id, first_name = message.from_user.first_name, last_name = message.from_user.last_name, chat_id=message.chat.id)
    # bot.delete_message(message.chat.id, message.message_id) 
    bot.send_message(message.chat.id, f"Привет {message.from_user.full_name}")

# class Mail:
#     def __init__(self):
#         self.description=None

# mail= Mail()

# def get_message(message:types.Message):
#     mail.description=message.text
#     users= TelegramUser.objects.all()
#     for user in users:
#         bot.send_message(user.id_user, mail.description)
#     bot.send_message(message.chat.id, 'рассылка окончена')

# @bot.message_handler(commands=['mailing'])
# def send_mailing(message:types.Message):
#     if message.chat.id !=int(admin_id):
#         bot.send_message(message.chat.id, 'Это команда доступна толька админу')
#         return
#     msg=bot.send_message(message.chat.id, 'введите текст для рассылки: ')
#     bot.register_next_stop_handler(msg, get_message)


# def get_text(message):
#     bot.send_message(admin_id, message)

def get_message(text):
    for admin in admins:
        bot.send_message(admin.chat_id, text)


@bot.message_handler()  
def echo(message:types.Message):
    # bot.delete_message(message.chat.id, message.message_id)  
    bot.send_message(message.chat.id, "Я вас не понял")