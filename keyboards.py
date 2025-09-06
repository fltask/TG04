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

# Функция для создания динамической клавиатуры с опциями
def dynamic_inline_keyboard():
    """
    Создает inline-клавиатуру с опциями.
    Возвращает готовую клавиатуру для использования в боте.
    """
    # Создаем билдер для клавиатуры
    keyboard_builder = InlineKeyboardBuilder()
    
    # Список опций для создания кнопок
    options = [
        {"text": "Опция 1", "callback_data": "option1"},
        {"text": "Опция 2", "callback_data": "option2"}
    ]
    
    # Добавляем кнопки с помощью цикла
    for option in options:
        keyboard_builder.add(InlineKeyboardButton(
            text=option["text"], 
            callback_data=option["callback_data"]
        ))
    
    # Настраиваем расположение кнопок (2 кнопки в ряд)
    keyboard_builder.adjust(2)
    
    # Возвращаем готовую клавиатуру
    return keyboard_builder.as_markup()
