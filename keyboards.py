from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder


main_keyboard = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="Привет"), KeyboardButton(text="Пока")],
], resize_keyboard=True, one_time_keyboard=True)

links_keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Новости", url="https://ria.ru/"),
    InlineKeyboardButton(text="Музыка", url="https://music.yandex.ru/"),
    InlineKeyboardButton(text="Видео", url="https://rutube.ru/")],
])
