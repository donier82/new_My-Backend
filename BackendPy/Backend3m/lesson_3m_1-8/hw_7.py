
from email.message import EmailMessage
import logging
import sqlite3
import smtplib
from aiogram import Bot, Dispatcher, F, types
from aiogram.filters import Command
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
import asyncio
from config import token, smtp_sender, smtp_sender_password

logging.basicConfig(level=logging.INFO)

bot = Bot(token=token)
storage = MemoryStorage()
dp = Dispatcher(storage=storage)

conn = sqlite3.connect('emails.db')
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS emails
              (id INTEGER PRIMARY KEY, email TEXT, subject TEXT, message TEXT)''')
conn.commit()

class Form(StatesGroup):
    EMAIL = State()
    SUBJECT = State()
    MESSAGE = State()

@dp.message(Command('start'))
async def cmd_start(message: types.Message, state: FSMContext):
    await state.set_state(Form.EMAIL)
    await message.reply("Привет! Пожалуйста, отправьте ваш Gmail адрес:")

@dp.message(Form.EMAIL)
async def process_email(message: types.Message, state: FSMContext):
    email = message.text
    await state.update_data(email=email)
    await state.set_state(Form.SUBJECT)
    await message.reply("Теперь введите тему письма:")

@dp.message(Form.SUBJECT)
async def process_subject(message: types.Message, state: FSMContext):
    subject = message.text
    await state.update_data(subject=subject)
    await state.set_state(Form.MESSAGE)
    await message.reply("И наконец, введите ваше сообщение:")

@dp.message(Form.MESSAGE)
async def process_message(message: types.Message, state: FSMContext):
    message_text = message.text
    user_data = await state.get_data()
    email = user_data['email']
    subject = user_data['subject']

    cursor.execute("INSERT INTO emails (email, subject, message) VALUES (?, ?, ?)", (email, subject, message_text))
    conn.commit()

    try:
        send_email(email, subject, message_text)
        await message.reply("Ваше сообщение успешно отправлено и сохранено в базе данных.")
    except Exception as e:
        await message.reply(f"Произошла ошибка при отправке письма: {str(e)}")

    await state.clear()

def send_email(to_email, subject, message_text):
    sender = smtp_sender
    password = smtp_sender_password

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()

    try:
        server.login(sender, password)
        msg = EmailMessage()
        msg['Subject'] = subject
        msg['From'] = sender
        msg['To'] = to_email

        msg.get_content(message_text)
        server.send_message(msg)
        return '200 OK'
    except Exception as error:
        return f"Error {error}"

async def main():   
    await bot.delete_webhook()
    await dp.start_polling(bot)
 

if __name__ == '__main__':
    asyncio.run(main())
