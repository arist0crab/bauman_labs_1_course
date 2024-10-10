"""
Бондарева Варвара ИУ7-14Б
Лабораторная работа #3
"""

from math import sqrt, isclose

# Ввод координат первой точки
x1 = float(input('Введите координату "x" 1 точки: '))
y1 = float(input('Введите координату "y" 1 точки: '))
# Ввод координат второй точки
x2 = float(input('\nВведите координату "x" 2 точки: '))
y2 = float(input('Введите координату "y" 2 точки: '))
# Ввод координат третьей точки
x3 = float(input('\nВведите координату "x" 3 точки: '))
y3 = float(input('Введите координату "y" 3 точки: '))
# Ввод координат случайной точки
xp = float(input('\nВведите координату "x" вашей точки: '))
yp = float(input('Введите координату "y" вашей точки: '))
h1, h2, h3 = 0, 0, 0
min_side, semi_side, max_side, bis = 0, 0, 0, 0
blunt_angled, point_inside = False, False

# Вычисление длин сторон предполагаемого треугольника
side_1 = sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
side_2 = sqrt((x3 - x2) ** 2 + (y3 - y2) ** 2)
side_3 = sqrt((x1 - x3) ** 2 + (y1 - y3) ** 2)
# Проверка, что треугольник вообще существует
is_triangle = (side_1 + side_2 > side_3 and side_1 + side_3 > side_2 and
               side_2 + side_3 > side_2)
if is_triangle:
    min_side, semi_side, max_side = sorted([side_1, side_2, side_3])
    # Вычисление длины биссектрисы, проведенной из меньшего угла
    bis = sqrt(semi_side * max_side * (semi_side + max_side + min_side) *
               (semi_side + max_side - min_side)) / (semi_side + max_side)
    # Определяем, является ли треугольник тупоугольным
    blunt_angled = max_side ** 2 > (min_side ** 2 + semi_side ** 2)
    # Вычисление площади большого треугольника по ф-ле Герона
    semi_perimetr = (min_side + semi_side + max_side) / 2
    big_square = sqrt(semi_perimetr * (semi_perimetr - min_side) *
                      (semi_perimetr - semi_side) * (semi_perimetr - max_side))
    # Вычисление площадей маленьких треугольников
    # Маленький треугольник 1 (точки 1 и 2)
    side_1 = sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    side_2 = sqrt((x2 - xp) ** 2 + (y2 - yp) ** 2)
    side_3 = sqrt((x1 - xp) ** 2 + (y1 - yp) ** 2)
    min_semi_perimetr = (side_1 + side_2 + side_3) / 2
    square_1 = sqrt(min_semi_perimetr * (min_semi_perimetr - side_1) *
                    (min_semi_perimetr - side_2) * (min_semi_perimetr - side_3))
    # Маленький треугольник 1 (точки 2 и 3)
    side_1 = sqrt((x2 - x3) ** 2 + (y2 - y3) ** 2)
    side_2 = sqrt((x2 - xp) ** 2 + (y2 - yp) ** 2)
    side_3 = sqrt((x3 - xp) ** 2 + (y3 - yp) ** 2)
    min_semi_perimetr = (side_1 + side_2 + side_3) / 2
    square_2 = sqrt(min_semi_perimetr * (min_semi_perimetr - side_1) *
                    (min_semi_perimetr - side_2) * (min_semi_perimetr - side_3))
    # Маленький треугольник 1 (точки 3 и 1)
    side_1 = sqrt((x1 - x3) ** 2 + (y1 - y3) ** 2)
    side_2 = sqrt((x3 - xp) ** 2 + (y3 - yp) ** 2)
    side_3 = sqrt((x1 - xp) ** 2 + (y1 - yp) ** 2)
    min_semi_perimetr = (side_1 + side_2 + side_3) / 2
    square_3 = sqrt(min_semi_perimetr * (min_semi_perimetr - side_1) *
                    (min_semi_perimetr - side_2) * (min_semi_perimetr - side_3))
    point_inside = isclose(square_1 + square_2 + square_3, big_square)  # Точка лежит внутри треугольника
    if point_inside:
        # Найдем высоту треугольника, образованного точками 1, 2 и данной точкой
        h1 = square_1 / sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
        # Найдем высоту треугольника, образованного точками 2, 3 и данной точкой
        h2 = square_2 / sqrt((x2 - x3) ** 2 + (y2 - y3) ** 2)
        # Найдем высоту треугольника, образованного точками 1, 3 и данной точкой
        h3 = square_3 / sqrt((x3 - x1) ** 2 + (y3 - y1) ** 2)

# Вывод значений
if is_triangle:
    print('Сторона 1: ', min_side)
    print('Сторона 2: ', semi_side)
    print('Сторона 3: ', max_side)
    print('Длина биссектрисы меньшего угла: ', bis)
    print('Треугольник тупоугольный' if blunt_angled else 'Треугольник не тупоугольный')
    if point_inside:
        print('\nТочка находится внутри заданного треугольника')
        print('Расстояние до ближайшей стороны от точки - ', min([h1, h2, h3]))
    else:
        print('\nДанная точка лежит вне треугольника')
else:
    print('Данные точки не образуют треугольник')
