# запустить первый телеграмм бот
# в терминале создаем виртуальное окружение.(что бы не было конфликтов с внешными библиотеками и 
# система управление версиями)
# >pyhton -m venv venv
# > ./venv/Scripts/activate
# > pip install aiogram (удаление uninstall)
# что бы получить токен откроем телеграмм
# в поиске напишем: BotFather
# /start -напишем
# из спмска выбираем:
# /newbot- create a new bot
# придумаем название бота 
# donier
# потом придумаем username , который заканчивается bot
# doni_bot
# потом копируем токен 191454:AAGj4xwCLliC0rVjNYGgzR6lGgI4uxaKZxs и вставим где 
# bot = Bot(token='191454:AAGj4xwCLliC0rVjNYGgzR6lGgI4uxaKZxs')
# потом запускаем где:  (venv) ps c:\users\doni\desktop\Geeks> python lesson_1.py  
# из телеграм выбираем t.me/pythondoni_bot.        запустить и вводим /st
 
# примечание! если появится: выполнение сценариев отключено в этой системе-
# - >Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass написать в терминале.

import asyncio
import logging
from aiogram import Bot, Dispatcher
from aiogram.types import Message # type: ignore
from aiogram.filters import Command

bot = Bot(token='191454:AAGj4xwCLliC0rVjNYGgzR6lGgI4uxaKZxs')
dp = Dispatcher()

@dp.message(Command('st'))
async def start(message:Message):
    await message.answer("Привет, как дела, товарищи ?")
    
async def main():
    await dp.start_polling(bot)
    
if __name__ == "__main__":
    asyncio.run(main())
