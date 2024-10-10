"""
Бондарева Варвара ИУ7-14Б
Программа для определения положения точки на заданной области
"""

# Ввод значений координат
x = float(input('Введите значение координаты x: '))
y = float(input('Введите значение координаты y: '))
# Назначение строковых переменных
fail = '\nДанная точка заданной области не принадлежит'
success = '\nДанная точка принадлежит заданной области'

# Определение, к каким четверти принадлежит точка
if x > 0 and y > 0:  # I четверть
    if (x / 4 - 1 / 2) <= y <= (2 * x - 4):
        if x < 4:
            print(success)
        elif 4 <= x <= 5.75:
            if y <= -(x - 4) ** 2 + 4:
                print(success)
            else:
                print(fail)
        else:
            print(fail)
    else:
        print(fail)
elif x > 0 > y:  # II четверть
    if (2 * x - 4) >= y >= (x / 4 - 1 / 2):
        print(success)
    else:
        print(fail)
elif x < 0 and y < 0:  # III четверть
    if -0.75 * x - 4 <= y <= x / 4 - 1 / 2:
        print(success)
    else:
        print(fail)
elif x < 0 < y:  # IV четверть
    print(fail)
# Точка принадлежит осям -> 2 возможных частных случая
if (x == 2 and y == 0) or (x == 0 and y == -4):
    print(success)
else:
    print(fail)

