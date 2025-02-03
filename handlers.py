from aiogram import types
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from datetime import datetime
from database import add_task, mark_task_done, delete_task
from keyboards import get_main_keyboard
from database import get_tasks

class TaskState(StatesGroup):
    title = State()
    description = State()
    deadline = State()
    mark_done_awaiting_id = State()
    delete_task_awaiting_id = State()

async def start(message: types.Message):
    await message.answer(
        "👋 Привет! Я бот для управления задачами. Выберите действие:",
        reply_markup=get_main_keyboard()
    )

async def process_new_task(message: types.Message, state: FSMContext):
    await message.answer("Введите заголовок задачи:")
    await state.set_state(TaskState.title)

async def get_task_title(message: types.Message, state: FSMContext):
    await state.update_data(title=message.text)
    await message.answer("Введите описание задачи:")
    await state.set_state(TaskState.description)

async def get_task_description(message: types.Message, state: FSMContext):
    await state.update_data(description=message.text)
    await message.answer("Введите дедлайн (YYYY-MM-DD):")
    await state.set_state(TaskState.deadline)

async def get_task_deadline(message: types.Message, state: FSMContext):
    user_data = await state.get_data()
    title, description, deadline = user_data["title"], user_data["description"], message.text

    try:
        deadline_date = datetime.strptime(deadline, "%Y-%m-%d").date()
        if deadline_date < datetime.now().date():
            await message.answer("❌ Дедлайн не может быть в прошлом!")
            return
    except ValueError:
        await message.answer("❌ Неверный формат даты! (YYYY-MM-DD)")
        return

    add_task(title, description, deadline)
    await message.answer(f"✅ Задача '{title}' добавлена!", reply_markup=get_main_keyboard())
    await state.clear()


async def list_tasks(message: types.Message):
    tasks = get_tasks()

    if not tasks:
        await message.answer("📭 У вас нет задач.")
        return

    response = "📋 Ваши задачи:\n\n"
    for task in tasks:
        task_id, title, description, deadline, status = task
        response += f"🆔 {task_id} | 📌 {title}\n📖 {description}\n⏳ Дедлайн: {deadline}\n🔹 Статус: {status}\n\n"

    await message.answer(response)

async def complete_task(message: types.Message, state: FSMContext):
    await message.answer("Введите ID задачи для завершения:")
    await state.set_state(TaskState.mark_done_awaiting_id)

async def mark_task_done_handler(message: types.Message, state: FSMContext):
    try:
        task_id = int(message.text)
        mark_task_done(task_id)
        await message.answer(f"✅ Задача {task_id} завершена!", reply_markup=get_main_keyboard())
    except ValueError:
        await message.answer("❌ Неверный ID задачи.")
    await state.clear()

async def delete_task_handler(message: types.Message, state: FSMContext):
    await message.answer("Введите ID задачи для удаления:")
    await state.set_state(TaskState.delete_task_awaiting_id)

async def confirm_delete_task(message: types.Message, state: FSMContext):
    try:
        task_id = int(message.text)
        delete_task(task_id)
        await message.answer(f"🗑 Задача {task_id} удалена!", reply_markup=get_main_keyboard())
    except ValueError:
        await message.answer("❌ Неверный ID задачи.")
    await state.clear()