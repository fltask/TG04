import os
import logging
from dotenv import load_dotenv

# Настраиваем логирование ПЕРЕД всеми импортами
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

from aiogram import Bot, Dispatcher, F
from aiogram.fsm.context import FSMContext
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, BotCommand
import keyboards as kb
import asyncio
import sys


# Загрузка токена из файла .env
load_dotenv()
TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

if not TOKEN:
    raise ValueError("TELEGRAM_BOT_TOKEN не найден в переменных окружения")

# Инициализация бота и диспетчера
bot = Bot(token=TOKEN)
dp = Dispatcher()


# /start
@dp.message(CommandStart())
async def start_command(message: Message, state: FSMContext):
    # Отправляем приветственное сообщение
    await message.answer(f"Привет, {message.from_user.username}! Добро пожаловать в бот, который показывает работу с кнопками", reply_markup=kb.main_keyboard)

@dp.message(Command("help"))
async def help_command(message: Message):
     await message.answer('''Я бот для демонстрации работы с кнопками.
Для начала работы, пожалуйста, введите команду /start.''')

@dp.message(F.text == "Привет")
async def hello_command(message: Message):
    await message.answer(f"Привет, {message.from_user.first_name}!")

@dp.message(F.text == "Пока")
async def goodbye_command(message: Message):
    await message.answer(f"До свидания, {message.from_user.first_name}!")

@dp.message(Command("links"))
async def links_command(message: Message):
    await message.answer(f"URL-ссылки:", reply_markup=kb.links_keyboard)


@dp.startup()
async def on_startup(bot: Bot):
    await bot.set_my_commands([
        BotCommand(command="start", description="Начать работу с ботом"),
        BotCommand(command="help", description="Справка"),
        BotCommand(command="links", description="URL-ссылки"),
    ])

async def main():
    # Запускаем бота
    try:
        await dp.start_polling(bot, polling_timeout=30)
    except Exception as e:
        print(f"Ошибка при запуске бота: {e}")
        await bot.close()


if __name__ == "__main__":
    print("Бот запущен!")
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Бот остановлен!")
        asyncio.run(bot.close())
        sys.exit()