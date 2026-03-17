# Функция расчета скидки с учетом категории пользователя
def calculate_discount(price, user_type):
    # Базовая скидка отсутствует
    discount = 0
    
    # VIP-клиенты получают повышенную скидку
    if user_type == "vip":
        discount = 0.1
    
    # Скидка для студентов - маркетинговая акция
    elif user_type == "student":
        discount = 0.05
    
    final_price = price * (1 - discount)
    return final_price


# TODO: Устаревшая функция. Будет удалена после миграции
def old_calculate(price):
    return price * 0.9


# Пример использования
if __name__ == "__main__":
    print("Тестирование функций скидок:")
    print(f"VIP клиент (1000): {calculate_discount(1000, 'vip')}")
    print(f"Студент (1000): {calculate_discount(1000, 'student')}")
    print(f"Обычный клиент (1000): {calculate_discount(1000, 'regular')}")
    print(f"Старая функция (1000): {old_calculate(1000)}")