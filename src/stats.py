"""
Модуль статистики для анализа истории конвертаций
Разработчик: [Прохорович Дарья]
"""

import json
from collections import Counter

HISTORY_FILE = "history.json"


def get_most_popular_bases():
    """
    Анализирует, какие системы счисления чаще всего использовались
    """
    try:
        with open(HISTORY_FILE, "r", encoding="utf-8") as f:
            history = json.load(f)
    except FileNotFoundError:
        print("Файл истории не найден. Сначала сделайте несколько конвертаций.")
        return None
    except json.JSONDecodeError:
        print("Ошибка чтения файла истории.")
        return None

    if not history:
        print("История пуста. Сначала сделайте несколько конвертаций.")
        return None

    input_bases = [record["input"]["base"] for record in history]
    output_bases = [record["output"]["base"] for record in history]
    all_bases = input_bases + output_bases

    counter = Counter(all_bases)

    print("\n" + "=" * 50)
    print("СТАТИСТИКА ИСПОЛЬЗОВАНИЯ СИСТЕМ СЧИСЛЕНИЯ")
    print("=" * 50)
    for base, count in counter.most_common():
        base_name = {
            2: "двоичная",
            8: "восьмеричная",
            10: "десятичная",
            16: "шестнадцатеричная",
        }.get(base, f"base-{base}")
        print(f"Основание {base} ({base_name}): {count} раз(а)")
    print("=" * 50)

    return counter


def get_conversion_frequency():
    """
    Показывает статистику по количеству конвертаций
    """
    try:
        with open(HISTORY_FILE, "r", encoding="utf-8") as f:
            history = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        print("История пуста или не найдена.")
        return

    print("\n" + "=" * 50)
    print("СТАТИСТИКА КОНВЕРТАЦИЙ")
    print("=" * 50)
    print(f"Всего конвертаций в истории: {len(history)}")
    print(f"Максимум хранимых записей: 10")

    if len(history) == 10:
        print("История полная (достигнут лимит в 10 записей)")
    else:
        print(f"Можно добавить ещё {10 - len(history)} записей")

    if len(history) > 1:
        first_date = history[-1]["timestamp"].split()[0]
        last_date = history[0]["timestamp"].split()[0]
        if first_date == last_date:
            print(f"Все конвертации сделаны {first_date}")
        else:
            print(f"Период: с {first_date} по {last_date}")
    print("=" * 50)


def find_longest_conversion():
    """
    Находит конвертацию с самым длинным результатом
    """
    try:
        with open(HISTORY_FILE, "r", encoding="utf-8") as f:
            history = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        print("История пуста или не найдена.")
        return

    if not history:
        print("Нет записей в истории")
        return

    longest = max(history, key=lambda x: len(x["output"]["value"]))

    print("\n" + "=" * 50)
    print("САМАЯ ДЛИННАЯ КОНВЕРТАЦИЯ")
    print("=" * 50)
    print(f"Время: {longest['timestamp']}")
    print(f"Вход: {longest['input']['value']} (base-{longest['input']['base']})")
    print(f"Выход: {longest['output']['value']} (base-{longest['output']['base']})")
    print(f"Длина результата: {len(longest['output']['value'])} символов")
    print("=" * 50)


def show_all_stats():
    """
    Показывает всю статистику сразу
    """
    print("\n" + "=" * 50)
    print("ВСЯ СТАТИСТИКА КОНВЕРТАЦИЙ")
    print("=" * 50)

    get_most_popular_bases()
    get_conversion_frequency()
    find_longest_conversion()


# Для самопроверки
if __name__ == "__main__":
    print("Тестирование модуля статистики...")
    show_all_stats()
