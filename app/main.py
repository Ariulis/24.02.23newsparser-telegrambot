import asyncio
from aiogram import types, Bot
from aiogram.dispatcher import Dispatcher
from aiogram.dispatcher.filters import Text
from aiogram.utils import executor
from aiogram.utils.markdown import hbold, hlink

from scraper import NewsParser
from misc import TELEGRAM_TOKEN, USER_ID, read_json

bot = Bot(TELEGRAM_TOKEN, parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot)


@dp.message_handler(commands='start')
async def start(message=types.Message):
    start_buttons = ['All the news', 'The freshes news', '5 latest news']
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(*start_buttons)
    answer = 'The news ribbon...'
    await message.answer(answer, reply_markup=keyboard)


@dp.message_handler(Text(equals='All the news'))
async def get_all_news(message=types.Message):
    parser = NewsParser()
    parser.get_data()
    
    data = read_json()

    i = 1
    for k, v in data.items():
        if i <= 5:
            news = f'{hbold(v["date"])}\n{hlink(v["title"], v["link"])}\n'
            await message.answer(news)
            await asyncio.sleep(1)
        i += 1


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
