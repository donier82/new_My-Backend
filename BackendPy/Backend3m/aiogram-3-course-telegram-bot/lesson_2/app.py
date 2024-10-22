import asyncio,logging
from aiogram import Bot, Dispatcher, types 
from aiogram.filters import CommandStart 
 
logging.basicConfig(level=logging.INFO)

bot = Bot(token="7301331561:AAH4j0tWAo0T0JxsAx4-b-sVwLfV2KoGv9o")
dp = Dispatcher()


@dp.message(CommandStart())
async def start_cmd(message: types.Message):
    await message.answer('Это была команда старт')
    

@dp.message()
async def echo(message: types.Message):

    await message.answer(message.text)
    await message.reply(message.text)


async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

asyncio.run(main())