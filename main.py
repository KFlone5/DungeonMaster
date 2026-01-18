from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart
import asyncio
import json

TOKEN = "8517893941:AAGlOUONxP1dJ8PexJ6VQrDzS1yI_7e4ZUg"
WEB_APP_URL = "https://kflone5.github.io/DungeonMaster/"  # ← обязательно измени на свой реальный URL!

bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message(CommandStart())
async def start_handler(message: types.Message):
    # Создаём клавиатуру с кнопкой Web App
    keyboard = types.ReplyKeyboardMarkup(
        resize_keyboard=True,
        one_time_keyboard=False,  # можно оставить, чтобы кнопка не пропадала
        keyboard=[
            [
                types.KeyboardButton(
                    text="Открыть Kronos Mini App 🚀",
                    web_app=types.WebAppInfo(url=WEB_APP_URL)
                )
            ]
        ]
    )
    
    await message.answer(
        "Привет! Бот в разработке, но уже можно открыть Mini App.\n\n"
        "Нажми кнопку ниже 👇",
        reply_markup=keyboard
    )

# Обработчик ЛЮБОГО сообщения (включая данные из Web App)
@dp.message()
async def handle_all_messages(message: types.Message):
    # Проверяем, пришли ли данные из Mini App
    if message.web_app_data:
        try:
            # Данные приходят как строка → пробуем распарсить как JSON
            data = json.loads(message.web_app_data.data)
            action = data.get("action", "неизвестно")
            
            await message.answer(
                f"Получены данные из Mini App!\n"
                f"Действие: {action}\n"
                f"Текст кнопки: {message.web_app_data.button_text}"
            )
        except json.JSONDecodeError:
            # Если не JSON — просто покажем сырые данные
            await message.answer(
                f"Данные из Mini App (сырые):\n"
                f"{message.web_app_data.data}"
            )
    else:
        # Обычное сообщение от пользователя
        await message.answer("Bot is currently under development...\n\nНо ты можешь открыть приложение кнопкой выше!")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())