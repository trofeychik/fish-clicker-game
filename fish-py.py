from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
import asyncio
import json
import os

BOT_TOKEN = '7948642582:AAGj_Sc36_IDuFl2xfy9piaGd-QMBJ3TeEE'

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

DATA_FILE = 'users_data.json'

def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r') as f:
            return json.load(f)
    return {}

def save_data(data):
    with open(DATA_FILE, 'w') as f:
        json.dump(data, f)

@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer(
        "Привет! Нажми /game, чтобы поиграть в кликер на рыбе."
    )

@dp.message(Command("game"))
async def cmd_game(message: types.Message):
    keyboard = types.InlineKeyboardMarkup(
        inline_keyboard=[
            [types.InlineKeyboardButton(text="🎮 Играть в кликер", web_app=types.WebAppInfo(url="https://trofeychik.github.io/-/"))]
        ]
    )
    await message.answer("Нажми кнопку ниже, чтобы начать игру!", reply_markup=keyboard)

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())