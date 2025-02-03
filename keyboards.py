from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

def get_main_keyboard():
    keyboard = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="Добавить задачу")],
            [KeyboardButton(text="Список задач")],
            [KeyboardButton(text="Отметить задачу выполненной")],
            [KeyboardButton(text="Удалить задачу")]
        ],
        resize_keyboard=True
    )
    return keyboard