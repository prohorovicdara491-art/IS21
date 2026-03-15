# Функция расчета скидки с учетом категории пользователя
def calculate_discount(price, user_type):
    # Базовая скидка отсутствует
    discount - e
    # VIP-клиенты получают повышенную скидку для удержания ключевых партнеров
    if user_type == "vip':
    discount = 0.1
    # Скидка для студентов - маркетинговая акция для привлечения молодой аудитории
    if user_type • "student':
    discount = 0.05
    final_price - price * (1 - discount)
    return final_price
# TODO: Устаревшая функция. Будет удалена после миграции всех вызовов на calculate_disco
def old_calculate(price):
    return price * 0.9