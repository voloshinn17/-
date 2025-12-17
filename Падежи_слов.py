сases_of_the_day = ('день', 'дня', 'дней')
сases_of_the_hour = ('час', 'часа', 'часов')
сases_of_the_minute = ('минута', 'минуты', 'минут')

# закидываем число и кортеж со склонениями

def choose_plural(amount, declensions):
    if amount % 100 in [11, 12, 13, 14] or amount % 10 >= 5 or amount % 10 == 0:
        return f"{amount} {declensions[2]}"
    elif amount % 10 == 1:
        return f"{amount} {declensions[0]}"
    elif 2 <= amount % 10 <= 4:
        return f"{amount} {declensions[1]}"
