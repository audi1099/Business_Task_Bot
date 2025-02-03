import asyncio
from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from handlers import *
from database import create_tables
from config import TOKEN
import os
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("TOKEN")
print("Запуск бота с ключом:", TOKEN)

bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
dp = Dispatcher()

dp.message.register(start, Command("start"))
dp.message.register(process_new_task, lambda message: message.text == "Добавить задачу")
dp.message.register(get_task_title, TaskState.title)
dp.message.register(get_task_description, TaskState.description)
dp.message.register(get_task_deadline, TaskState.deadline)
dp.message.register(complete_task, lambda message: message.text == "Отметить задачу выполненной")
dp.message.register(mark_task_done_handler, TaskState.mark_done_awaiting_id)
dp.message.register(delete_task_handler, lambda message: message.text == "Удалить задачу")
dp.message.register(confirm_delete_task, TaskState.delete_task_awaiting_id)
dp.message.register(list_tasks, lambda message: message.text == "Список задач")

async def main():
    create_tables()
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())