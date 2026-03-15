"""
Модуль А: Конвертер чисел между системами счисления (2, 8, 10, 16)
Разработчик: [Васильев]
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
            return bin(decimal_number)[2:]  # [2:] отрезает префикс '0b'
        elif to_base == 8:
            return oct(decimal_number)[2:]  # [2:] отрезает префикс '0o'
        elif to_base == 16:
            return hex(decimal_number)[2:].upper()  # [2:] отрезает '0x', .upper() для заглавных букв
        else:
            return "Ошибка: неподдерживаемая система счисления"

    except ValueError as e:
        return f"Ошибка конвертации: {e}"

# Пример использования модуля (для самопроверки)
if __name__ == "__main__":
    print("Тестирование модуля А (конвертер):")

    test_cases = [
        ("1010", 2, 10),  # 1010(2) -> 10(10)
        ("FF", 16, 10),  # FF(16) -> 255(10)
        ("255", 10, 16),  # 255(10) -> FF(16)
        ("777", 8, 2),   # 777(8) -> 111111111(2)
    ]

    for num, from_b, to_b in test_cases:
        result = convert_number(num, from_b, to_b)
        print(f"{num} (base={from_b}) -> {result} (base={to_b})")