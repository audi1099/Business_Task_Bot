import sqlite3


def create_tables():
    conn = sqlite3.connect("tasks.db")
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            user_id INTEGER PRIMARY KEY,
            registered INTEGER DEFAULT 0,
            register_code TEXT
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT,
            description TEXT,
            deadline TEXT,
            status TEXT DEFAULT 'new'
        )
    """)

    conn.commit()
    conn.close()


def add_task(title, description, deadline):
    try:
        conn = sqlite3.connect("tasks.db")
        cursor = conn.cursor()
        cursor.execute("INSERT INTO tasks (title, description, deadline) VALUES (?, ?, ?)",
                       (title, description, deadline))
        conn.commit()
    except sqlite3.Error as e:
        print(f"Ошибка базы данных: {e}")
    finally:
        conn.close()


def get_tasks():
    conn = sqlite3.connect("tasks.db")
    cursor = conn.cursor()
    cursor.execute("SELECT id, title, description, deadline, status FROM tasks")
    tasks = cursor.fetchall()
    conn.close()
    return tasks


def mark_task_done(task_id):
    try:
        conn = sqlite3.connect("tasks.db")
        cursor = conn.cursor()
        cursor.execute("UPDATE tasks SET status='completed' WHERE id=?", (task_id,))
        conn.commit()
    except sqlite3.Error as e:
        print(f"Ошибка базы данных: {e}")
    finally:
        conn.close()


def delete_task(task_id):
    try:
        conn = sqlite3.connect("tasks.db")
        cursor = conn.cursor()
        cursor.execute("DELETE FROM tasks WHERE id=?", (task_id,))
        conn.commit()
    except sqlite3.Error as e:
        print(f"Ошибка базы данных: {e}")
    finally:
        conn.close()