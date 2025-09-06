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

dynamic_keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Показать больше", callback_data="show_more")],
])

dynamic_inline_keyboard = InlineKeyboardBuilder()
dynamic_inline_keyboard.add(InlineKeyboardButton(text="Опция 1", callback_data="option1"))
dynamic_inline_keyboard.add(InlineKeyboardButton(text="Опция 2", callback_data="option2"))
dynamic_inline_keyboard.adjust(2)
