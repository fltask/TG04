# Импорт стандартных библиотек
import os
import logging
import asyncio
import sys

# Импорт библиотеки для работы с переменными окружения
from dotenv import load_dotenv

# Настраиваем логирование ПЕРЕД всеми импортами
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

# Импорт компонентов aiogram для работы с Telegram Bot API
from aiogram import Bot, Dispatcher, F
from aiogram.fsm.context import FSMContext
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, BotCommand, CallbackQuery

# Импорт модуля с клавиатурами
import keyboards as kb


# Загрузка токена из файла .env
load_dotenv()
TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

# Проверка наличия токена
if not TOKEN:
    raise ValueError("TELEGRAM_BOT_TOKEN не найден в переменных окружения")

# Инициализация бота и диспетчера
bot = Bot(token=TOKEN)
dp = Dispatcher()


# Обработчик команды /start
@dp.message(CommandStart())
async def start_command(message: Message, state: FSMContext):
    """
    Обработчик команды /start.
    Отправляет приветственное сообщение с основной клавиатурой.
    """
    # Отправляем приветственное сообщение с основной клавиатурой
    await message.answer(
        f"Привет, {message.from_user.username}! Добро пожаловать в бот, который показывает работу с кнопками", 
        reply_markup=kb.main_keyboard
    )

# Обработчик команды /help
@dp.message(Command("help"))
async def help_command(message: Message):
    """
    Обработчик команды /help.
    Показывает справку по использованию бота.
    """
    await message.answer('''Я бот для демонстрации работы с кнопками.
Для начала работы, пожалуйста, введите команду /start.''')

# Обработчик нажатия кнопки "Привет"
@dp.message(F.text == "Привет")
async def hello_command(message: Message):
    """
    Обработчик нажатия кнопки "Привет" из основной клавиатуры.
    Отвечает приветствием пользователю.
    """
    await message.answer(f"Привет, {message.from_user.first_name}!")

# Обработчик нажатия кнопки "Пока"
@dp.message(F.text == "Пока")
async def goodbye_command(message: Message):
    """
    Обработчик нажатия кнопки "Пока" из основной клавиатуры.
    Отвечает прощанием пользователю.
    """
    await message.answer(f"До свидания, {message.from_user.first_name}!")

# Обработчик команды /links
@dp.message(Command("links"))
async def links_command(message: Message):
    """
    Обработчик команды /links.
    Показывает inline-кнопки с URL-ссылками.
    """
    await message.answer("URL-ссылки:", reply_markup=kb.links_keyboard)

# Обработчик команды /dynamic
@dp.message(Command("dynamic"))
async def dynamic_command(message: Message):
    """
    Обработчик команды /dynamic.
    Показывает динамическую клавиатуру с кнопкой "Показать больше".
    """
    await message.answer("Динамическая клавиатура:", reply_markup=kb.dynamic_keyboard)
# Обработчик callback query для кнопки "Показать больше"
@dp.callback_query(F.data == "show_more")
async def show_more_callback(callback: CallbackQuery):
    """
    Обработчик нажатия кнопки "Показать больше".
    Заменяет клавиатуру на клавиатуру с опциями 1 и 2.
    """
    # Заменяем клавиатуру на новую с опциями
    await callback.message.edit_reply_markup(reply_markup=kb.dynamic_inline_keyboard.as_markup())
    # Подтверждаем получение callback query
    await callback.answer()

# Обработчик callback query для кнопки "Опция 1"
@dp.callback_query(F.data == "option1")
async def option1_callback(callback: CallbackQuery):
    """
    Обработчик нажатия кнопки "Опция 1".
    Показывает всплывающее уведомление и отправляет сообщение.
    """
    # Показываем всплывающее уведомление
    await callback.answer("Опция 1", show_alert=True)
    # Отправляем сообщение с текстом опции
    await callback.message.answer("Опция 1")

# Обработчик callback query для кнопки "Опция 2"
@dp.callback_query(F.data == "option2")
async def option2_callback(callback: CallbackQuery):
    """
    Обработчик нажатия кнопки "Опция 2".
    Показывает всплывающее уведомление и отправляет сообщение.
    """
    # Показываем всплывающее уведомление
    await callback.answer("Опция 2", show_alert=True)
    # Отправляем сообщение с текстом опции
    await callback.message.answer("Опция 2")

# Обработчик запуска бота
@dp.startup()
async def on_startup(bot: Bot):
    """
    Обработчик события запуска бота.
    Устанавливает меню команд для бота.
    """
    # Устанавливаем меню команд, которое будет отображаться в интерфейсе Telegram
    await bot.set_my_commands([
        BotCommand(command="start", description="Начать работу с ботом"),
        BotCommand(command="help", description="Справка"),
        BotCommand(command="links", description="URL-ссылки"),
        BotCommand(command="dynamic", description="Динамическая клавиатура"),
    ])

# Основная функция для запуска бота
async def main():
    """
    Основная функция для запуска бота.
    Запускает polling для получения обновлений от Telegram.
    """
    try:
        # Запускаем polling с таймаутом 30 секунд
        await dp.start_polling(bot, polling_timeout=30)
    except Exception as e:
        print(f"Ошибка при запуске бота: {e}")
        # Закрываем соединение с ботом при ошибке
        await bot.close()


# Точка входа в программу
if __name__ == "__main__":
    """
    Точка входа в программу.
    Запускает бота и обрабатывает прерывание клавиатурой.
    """
    print("Бот запущен!")
    try:
        # Запускаем асинхронную функцию main()
        asyncio.run(main())
    except KeyboardInterrupt:
        # Обрабатываем прерывание клавиатурой (Ctrl+C)
        print("Бот остановлен!")
        asyncio.run(bot.close())
        sys.exit()