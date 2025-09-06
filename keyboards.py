# Импорт типов клавиатур из aiogram
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
# Импорт билдеров для создания клавиатур
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder


# Основная reply-клавиатура с кнопками "Привет" и "Пока"
main_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Привет"), KeyboardButton(text="Пока")],
    ], 
    resize_keyboard=True,    # Автоматически изменяет размер кнопок
    one_time_keyboard=True   # Клавиатура исчезает после нажатия
)

# Inline-клавиатура с URL-ссылками
links_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Новости", url="https://ria.ru/"),
            InlineKeyboardButton(text="Музыка", url="https://music.yandex.ru/"),
            InlineKeyboardButton(text="Видео", url="https://rutube.ru/")
        ],
    ]
)

# Начальная динамическая клавиатура с кнопкой "Показать больше"
dynamic_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Показать больше", callback_data="show_more")],
    ]
)

# Создание динамической клавиатуры с помощью билдера
dynamic_inline_keyboard = InlineKeyboardBuilder()

# Добавляем кнопки с callback_data для обработки нажатий
dynamic_inline_keyboard.add(InlineKeyboardButton(text="Опция 1", callback_data="option1"))
dynamic_inline_keyboard.add(InlineKeyboardButton(text="Опция 2", callback_data="option2"))

# Настраиваем расположение кнопок (2 кнопки в ряд)
dynamic_inline_keyboard.adjust(2)
