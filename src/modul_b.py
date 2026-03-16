"""
Модуль B: Валидация ввода для разных систем счисления
Разработчик: [Куксенко]
"""

def validate_number(number_str, base):
    """
    Проверяет, соответствует ли строка указанной системе счисления.

    Параметры:
    number_str (str): Проверяемое число
    base (int): Основание системы счисления (2, 8, 10, 16)

    Возвращает:
    tuple: (bool, str) - (корректен ли ввод, сообщение об ошибке)
    """

    if not number_str:
        return False, "Число не может быть пустым"

    # Убираем возможный префикс 0x, 0b, 0o для проверки
    clean_str = number_str.upper()

    if clean_str.startswith(('0X', '0B', '0O')):
        clean_str = clean_str[2:]

    # Проверяем каждый символ
    valid_chars = get_valid_characters(base)

    for char in clean_str:
        if char not in valid_chars:
            return False, "Недопустимый символ '{}'".format(char)

    return True, "Число корректно"

def get_valid_characters(base):
    """
    Возвращает строку с допустимыми символами для указанного основания.
    """
    digits = "0123456789"
    letters = "ABCDEF"

    if base <= 10:
        return digits[:base]
    else:
        return digits + letters[:base-10]

# Пример использования модуля (для самопроверки)
if __name__ == "__main__":
    print("Тестирование модуля B (валидация):")
    test_cases = [
        ("10102", 2),  # Неверно (есть цифра 2)
        ("FF", 16),    # Верно
        ("128", 8),    # Неверно (есть цифра 8)
        ("13F", 16),   # Верно
        ("1010", 2),   # Верно
    ]

    for num, base in test_cases:
        is_valid, message = validate_number(num, base)
        result = "✓" if is_valid else "X"
        print(f"{result} {num} (base={base}) = {message}")

        def validate_file(filename, base):
    """   Проверяет все числа в файле
    """
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            lines = f.readlines()
    except FileNotFoundError:
        return [("Файл не найден", False, "Ошибка: файл отсутствует")]
    
    results = []
    for i, line in enumerate(lines, 1):
        line = line.strip()
        if line:  # если строка не пустая
            is_valid, msg = validate_number(line, base)
            results.append((f"Строка {i}: {line}", is_valid, msg))
    
    return results