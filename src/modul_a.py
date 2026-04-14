"""
Модуль А: Конвертер чисел между системами счисления (2, 8, 10, 16)
Разработчик: [Тимофей]
"""


def convert_number(number_str, from_base, to_base):
    """
    Конвертирует число из одной системы счисления в другую.

    Параметры:
    number_str (str): Число в виде строки
    from_base (int): Исходное основание (2, 8, 10, 16)
    to_base (int): Целевое основание (2, 8, 10, 16)

    Возвращает:
    str: Число в целевой системе счисления
    """
    try:
        # Сначала переводим в десятичную систему
        decimal_number = int(number_str, from_base)

        # Затем из десятичной в целевую систему
        if to_base == 10:
            return str(decimal_number)
        elif to_base == 2:
            return bin(decimal_number)[2:]
        elif to_base == 8:
            return oct(decimal_number)[2:]
        elif to_base == 16:
            return hex(decimal_number)[2:].upper()
        else:
            return "Ошибка: неподдерживаемая система счисления"
    except ValueError as e:
        return f"Ошибка конвертации: {e}"


def batch_convert(numbers_list, from_base, to_base):
    """
    Конвертирует несколько чисел за раз.

    Параметры:
    numbers_list (list): Список строк с числами
    from_base (int): Исходное основание
    to_base (int): Целевое основание

    Возвращает:
    list: Список результатов конвертации
    """
    results = []
    for num in numbers_list:
        try:
            result = convert_number(num, from_base, to_base)
            results.append(result)
        except Exception as e:
            results.append(f"Ошибка: {e}")
    return results


# Пример использования модуля (для самопроверки)
if __name__ == "__main__":
    print("Тестирование модуля А (конвертер):")

    # Тесты для convert_number
    test_cases = [
        ("1010", 2, 10),  # 1010(2) -> 10(10)
        ("FF", 16, 10),  # FF(16) -> 255(10)
        ("255", 10, 16),  # 255(10) -> FF(16)
        ("777", 8, 2),  # 777(8) -> 111111111(2)
    ]

    print("\n--- Тест convert_number ---")
    for num, from_b, to_b in test_cases:
        result = convert_number(num, from_b, to_b)
        print(f"{num} (base={from_b}) -> {result} (base={to_b})")

    # Тесты для batch_convert
    print("\n--- Тест batch_convert ---")
    numbers = ["1010", "FF", "777", "123"]
    results = batch_convert(numbers, 16, 10)
    for original, converted in zip(numbers, results):
        print(f"{original} (base=16) -> {converted} (base=10)")
