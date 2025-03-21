# Telegram Bot - Task Manager

Этот бот предназначен для управления задачами в Telegram. Он позволяет добавлять, просматривать, отмечать выполненные и удалять задачи.

## 📌 Функционал
- Добавление задач
- Просмотр списка задач
- Отметка выполненных задач
- Удаление задач
- Авторизация по номерам телефонов

---

## 🔧 Установка и настройка

### 1️⃣ Клонирование репозитория
```sh
git clone <URL-РЕПОЗИТОРИЯ>
cd <ИМЯ-ПАПКИ>
```

### 2️⃣ Установка зависимостей
Создайте и активируйте виртуальное окружение (рекомендуется):
```sh
python -m venv venv
source venv/bin/activate  # Для Linux/Mac
venv\Scripts\activate  # Для Windows
```

Затем установите зависимости:
```sh
pip install -r requirements.txt
```

### 3️⃣ Настройка переменных окружения
Создайте `.env` файл и добавьте в него:
```ini
TOKEN=ВАШ_ТОКЕН_БОТА
```

### 4️⃣ Запуск базы данных
Бот использует базу данных SQLite. Перед запуском создайте таблицы:
```sh
python -c "from database import create_tables; create_tables()"
```

---

## 🚀 Запуск бота
Запустите бота командой:
```sh
python main.py
```

---

## 📂 Структура проекта
```
📦 telegram-task-bot
├── 📜 config.py          # Конфигурация бота
├── 📜 database.py        # Управление базой данных
├── 📜 handlers.py        # Обработчики команд
├── 📜 main.py            # Основной файл для запуска бота
├── 📜 requirements.txt   # Зависимости проекта
└── 📜 .env               # Переменные окружения
```

---

## 🛠 Разработка
При изменении кода рекомендуется перезапускать бота после внесения изменений.

---

## 📞 Авторизация пользователей
Бот поддерживает авторизацию через список разрешенных номеров. Для добавления номеров используйте файл `authorized_phones.txt`, добавляя один номер в строку.

Пример содержимого файла:
```
+375291234567
+375441234567
```

---

## 📌 Контакты
Если у вас есть вопросы или предложения, свяжитесь со мной!

