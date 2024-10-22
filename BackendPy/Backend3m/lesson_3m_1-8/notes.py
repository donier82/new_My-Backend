from aiogram import Bot, Dispatcher, types, F
from aiogram.types import Message
from aiogram.filters import Command

from config import token
import logging, sqlite3, time, asyncio

bot = Bot(token=token)
dp = Dispatcher()

logging.basicConfig(level=logging.INFO)

connection = sqlite3.connect("notes.db")
cursor = connection.cursor()
cursor.execute("""CREATE TABLE IF NOT EXISTS kitay(
    id INT,
    username VARCHAR(100),
    usersurname VARCHAR(100),
    phone TEXT
);
""")

@dp.message(Command('start'))
async def start(message:Message):
    await message.answer(f'Привет, {message.from_user.full_name}, отправь мне заметку, фамилия имя и телефон')

    
@dp.message()
async def save_note(message:Message):
    cursor.execute('INSERT INTO kitay(id, username, note) VALUES (?, ?, ?)', (message.username, message.surname, message.phone))
    connection.commit()
    await message.answer("данное  сохранена!")
    
async def main():
    await dp.start_polling(bot)
    
if __name__ == "__main__":
    asyncio.run(main())