"""
Бондарева Варвара ИУ7-14Б
Программа для определения положения точки на заданной области
"""

# Ввод значений координат.
# Могу себе позволить, т.к. рисунок симметричный
x = abs(float(input('Введите значение координаты x: ')))
y = float(input('Введите значение координаты y: '))
# Назначение строковых переменных
fail = '\nДанная точка заданной области не принадлежит'
success = '\nДанная точка принадлежит заданной области'

# Проверяем принадлежность осям координат, частные случаи
if (x == 0 and (y == 2 or y == -6)) or (x == 1 and y == 0):
    print(success)
else:
    # Проверяем усики
    if y == 3 / 2 * x + 2:
        print(success)
    else:
        if x == 1 and 0 < y <= -2:
            print(success)
        elif x < 1:
            if -4 * x ** 2 + 2 >= y >= 4 * x ** 2 - 6:
                print(success)
            else:
                print(fail)
        else:  # x > 1
            # Работаем в I четверти
            if y > 0:
                if x < 8:
                    if 1 / 49 * (x - 1) ** 2 <= y <= -1 / 8 * (x - 9) ** 2 + 8:
                        print(success)
                    else:
                        print(fail)
                elif 8 <= x <= 9:
                    if 7 * (x - 8) ** 2 + 1 <= y <= -1 / 8 * (x - 9) ** 2 + 8:
                        print(success)
                    else:
                        print(fail)
                else:
                    print(fail)
            # Работаем во II четверти
            else:
                if x < 2:
                    if -2 * (x - 1) ** 2 - 2 <= y <= -1 / 16 * x ** 2:
                        print(success)
                    else:
                        print(fail)
                elif 2 <= x <= 8:
                    if 1 / 3 * (x - 5) ** 2 - 7 <= y <= -1 / 16 * x ** 2:
                        print(success)
                    else:
                        print(fail)
                else:
                    print(fail)
