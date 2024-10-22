import smtplib, logging, F 
from email.message import EmailMessage
from aiogram import Bot, Dispatcher, types
from aiogram.types import Message
from aiogram import Router
from aiogram.filters import Command
from config import token, smtp_sender, smtp_sender_password
logging.basicConfig(level=logging.INFO)

smtp= 'smtp@gmail.com'
SMTP_PORT=587
SMTP_SENDER_EMAIL=smtp_sender 
SMTP_SENDER_PASSWORD= smtp_sender_password 
bot=Bot(token=token)
dp=Dispatcher()

router=Router()

@router.message(Command('start'))
async def send_welcome(message:Message):
    await message.answer('hello world')
@router.message(Command('send_email'))
async def send_email(message:Message):
    to_email='recipient@exaple.com'
    subject='test message'
    bode='this is a text message'
    try:
        server=smtplib.SMTP()
        server.starttls()
         
        server.login(SMTP_SENDER)
        msg=EmailMessage()
        msg['From']=SMTP_SENDER_EMAIL