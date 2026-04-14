"""
Модуль C: История последних 10 конвертаций
Разработчик: [Прохорович]
"""

import json
import os
from datetime import datetime

HISTORY_FILE = "history.json"
MAX_HISTORY = 10


def load_history():
    """
    Загружает историю из файла.
    """
    if not os.path.exists(HISTORY_FILE):
        return []

    try:
        with open(HISTORY_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except (json.JSONDecodeError, FileNotFoundError):
        return []


def save_history(history):
    """
    Сохраняет историю в файл.
    """
    with open(HISTORY_FILE, "w", encoding="utf-8") as f:
        json.dump(history, f, ensure_ascii=False, indent=2)


def add_record(input_value, input_base, output_value, output_base):
    """
    Добавляет запись о конвертации в историю.
    """
    history = load_history()

    # Создаем новую запись
    record = {
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "input": {"value": input_value, "base": input_base},
        "output": {"value": output_value, "base": output_base},
    }

    # Добавляем новую запись в начало списка
    history.insert(0, record)

    # Оставляем только последние MAX_HISTORY записей
    history = history[:MAX_HISTORY]

    save_history(history)


def show_history():
    """
    Выводит всю историю конвертаций в читаемом виде.
    """
    history = load_history()

    if not history:
        print("История конвертаций пуста.")
        return

    print("\n" + "=" * 50)
    print("ИСТОРИЯ КОНВЕРТАЦИЙ (последние 10)")
    print("=" * 50)

    # Нумеруем записи с 1 (для пользователя) и показываем последние сверху
    for i, record in enumerate(history, 1):
        inp = record["input"]
        out = record["output"]
        print(f"{i:2d}. {record['timestamp']}")
        print(
            f"   {inp['value']} (base-{inp['base']}) -> {out['value']} (base-{out['base']})"
        )

    print("=" * 50 + "\n")


def clear_history():
    """
    Очищает всю историю.
    """
    save_history([])
    print("История конвертаций очищена.")


# Пример использования модуля (для самопроверки)
if __name__ == "__main__":
    print("Тестирование модуля C (история)...")

    # Очистим историю для чистоты теста
    clear_history()

    # Добавим несколько тестовых записей
    add_record("1010", 2, "10", 10)
    add_record("FF", 16, "255", 10)
    add_record("777", 8, "511", 10)
    add_record("123", 10, "1111011", 2)

    # Покажем историю
    show_history()

    print("Тест завершен. Модуль готов к интеграции.")
