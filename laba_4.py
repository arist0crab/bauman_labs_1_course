"""
Бондарева Варвара ИУ7-14Б
Лабораторная работа №5
Работа с графиками
"""
# Подключение необходимых библиотек
from math import isclose, inf


# Ввод переменных и констант
start_t = float(input('Введите начальное значение аргумента: '))
final_t = float(input('Введите конечное значение аргумента: '))
step_t = float(input('Введите шаг разбиения отрезка: '))
serifs = int(input('Введите количество засечек (от 4 до 8): '))
# Инициализация *типа* минимума и максимума функции
min_y = inf
max_y = -inf

# Защита от хомяков
while final_t <= start_t:
    print('Конечное значение должно быть больше, чем начальное')
    final_t = float(input('Еще раз введите конечное значение аргумента: '))
while (final_t - start_t < step_t) or step_t <= 0:
    if final_t - start_t < step_t:
        print('Шаг очень большой, шагайте меньше')
    elif step_t < 0:
        print('Шаг не может быть меньше 0')
    else:
        print('Шаг не может быть равен 0, мы так не уйдем никуда')
    step_t = float(input('Введите шаг разбиения отрезка: '))
while not (4 <= serifs <= 8):
    serifs = int(input('Я же сказала, от 4 до 8. Еще одна попытка: '))

# Составление таблицы
print('-' * 64)
print(f'|{'t':^30}|{'W':^30}|')
print('-' * 64)
iterations_col = int((final_t - start_t) // step_t) + 1
iterations_col += isclose(start_t + iterations_col * step_t, final_t)
t = start_t
for i in range(iterations_col):
    W = 2048 * t ** 12 - 6144 * t ** 10 - 3584 * t ** 6 + 840 * t ** 4 - 72 * t ** 2 + 1
    print('|{:^30}|{:^30.7g}|'.format('{:.7g}'.format(t), W))
    print(f'|{'{:.7g}'.format(t):^30}|{W:^30.7g}|')
    t = start_t + (i + 1) * step_t
    if max_y < W:
        max_y = W
    if min_y > W:
        min_y = W
else:
    print('-' * 64)

# Составление и отрисовка графика
print()
print(f'{'График типа':^90}')
print()

# Отрисовка оси y
y_value_step = (max_y - min_y) / (serifs - 1)  # y2 - y1 (засечки: y1 y2 y3 y4)
y_diff_btw_spaces = (max_y - min_y) / 80  # Численная разница между двумя соседними пробелами (из 80)
# Считает сколько пробелов должно быть между числами верхней строки оси y, если каждое из них занимает по 8 пробелов
space_btw_y = int((80 - serifs * 8) / (serifs - 1))
# Т.к. мы округляем в строчке 51, найдем оставшиеся неиспользованные пробелы
rest_spaces = (80 - serifs * 8) % (serifs - 1)
y_axis = ' ' * 9 + '|' + f'{min_y:8.4g}'  # Начало отрисовки оси y
y = min_y
for i in range(serifs - 2):
    y += y_value_step
    y_axis += ' ' * space_btw_y + f'{y:8.4g}'
y_axis += ' ' * space_btw_y + f'{max_y:{8 + rest_spaces}.4g}'
print(y_axis)
# Отрисовка клеточек графика
t = start_t
for i in range(iterations_col):
    W = 2048 * t ** 12 - 6144 * t ** 10 - 3584 * t ** 6 + 840 * t ** 4 - 72 * t ** 2 + 1
    star_num_spaces = int((W - min_y) / y_diff_btw_spaces) - 1  # Количество пробелов перед звездочкой
    x_stick_num = int(0 - min_y / y_diff_btw_spaces) - 1  # В теории количество пробелов перед палочкой
    x_axis = f'{t:^9.4g}|'
    if x_stick_num < 0:  # Если наша нулевая ось выходит за левую границу графика
        x_axis += ' ' * star_num_spaces + '*'
    else:
        if star_num_spaces < 0:
            star_num_spaces = 0
        if x_stick_num > star_num_spaces:  # Если * слева от |
            x_axis += ' ' * star_num_spaces + '*' + ' ' * (x_stick_num - star_num_spaces - 1) + '|'
        elif x_stick_num < star_num_spaces:  # Если * справа от |
            x_axis += ' ' * x_stick_num + '|' + ' ' * (star_num_spaces - x_stick_num) + '*'
        else:  # Если * накладывается на |
            x_axis += ' ' * x_stick_num + '*'
    print(x_axis)
    t = start_t + (i + 1) * step_t
