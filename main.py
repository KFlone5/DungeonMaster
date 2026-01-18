from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart
import asyncio

TOKEN = "8517893941:AAGlOUONxP1dJ8PexJ6VQrDzS1yI_7e4ZUg"

bot = Bot(token=TOKEN)
dp = Dispatcher()

# /start
@dp.message(CommandStart())
async def start_handler(message: types.Message):
    await message.answer("Bot is currently under development...")

# Ответ на любое сообщение
@dp.message()
async def echo_all(message: types.Message):
    await message.answer("Bot is currently under development...")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())