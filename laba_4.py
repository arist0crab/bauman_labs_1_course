# Подключение необходимых библиотек
from math import isclose


# Ввод переменных и констант
t = float(input('Введите начальное значение аргумента: '))
final_t = float(input('Введите конечное значение аргумента: '))
step_t = float(input('Введите шаг разбиения отрезка: '))
serifs = int(input('Введите количество засечек (от 4 до 8): '))
# Защита от хомяков
while not (4 <= serifs <= 8):
    serifs = int(input('Я же сказала, от 4 до 8. Еще одна попытка: '))

# Составление таблицы и графика
print('-' * 64)
print('|{:^30}|{:^30}|'.format('t', 'W'))
print('-' * 64)
iterations_col = int((final_t - t) // step_t) + 1
iterations_col += isclose(t + iterations_col * step_t, final_t)
for i in range(iterations_col):
    W = 2048 * t ** 12 - 6144 * t ** 10 - 3584 * t ** 6 + 840 * t ** 4 - 72 * t ** 2 + 1
    print('|{:^30}|{:^30.7g}|'.format(t, W))
    t = float('{:.7g}'.format(t + step_t))
else:
    print('-' * 64)
