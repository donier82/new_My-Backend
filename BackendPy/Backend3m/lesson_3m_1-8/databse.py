from aiogram import Bot, Dispatcher, types, F
from aiogram.types import Message
from aiogram.filters import Command

from config import token
import logging, sqlite3, time, asyncio

bot = Bot(token=token)
dp = Dispatcher()

logging.basicConfig(level=logging.INFO)

connection = sqlite3.connect("kitay.db")
cursor = connection.cursor()
cursor.execute("""CREATE TABLE IF NOT EXISTS users(
    id INT ,
    name VARCHAR(100),
    surname VARCHAR(100),
    phone INT  

);
""")

@dp.message(Command('start'))
async def start(message:Message):
    cursor.execute(f"SELECT id FROM users WHERE id = {message.from_user.id}")
    users_result = cursor.fetchall()
    print(users_result)
    if users_result == []:
        cursor.execute("INSERT INTO users VALUES (?, ?, ?);",
                    (personal_kod, adress, message_kitay))
        cursor.connection.commit()
    await message.reply(f'Привет, {message.from_user.full_name}')
    
async def main():
    await dp.start_polling(bot)
    
if __name__ == "__main__":
    asyncio.run(main())