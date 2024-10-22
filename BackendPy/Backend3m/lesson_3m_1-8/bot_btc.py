from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command, CommandStart
from aiogram.types import Message, BotCommand
from config import token
import requests, time, asyncio, aioschedule, logging

bot=Bot(token=token)
dp= Dispatcher()
logging.basicConfig(level=logging.INFO)

def get_btc_price():
    url='https://api.binance.com/api/v3/avgPrice?symbol=BTCUSDT'
    responce=requests.get(url=url).json()
    price= responce.get('price')
    if price:
        return f'стоимость биткоина на {time.ctime()},{price}'
    else:
        return f'не удалось полусить цену биткоина'
async def schedule():
    while monitoring:
        message=await get_btc_price()
        await bot.send_message(chat_id, message)
        await asyncio.sleep(1)

@dp.message(CommandStart())
async def start(message:Message):
    await message.answer(f'привет {message.from_user.full_name}')

@dp.message(Command('btc'))
async def bts(message:Message):
    global chat_id, monitoring
    chat_id=message.migrate_to_chat_id
    monitoring=True
    await message.answer('начало мониторинга')
    await schedule()

@dp.message(Command('stop'))
async def stop(message:Message):
    global monitoring
    monitoring=False
    await message.answer('мониторинг цены осьановлен')

