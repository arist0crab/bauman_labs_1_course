"""
Бондарева Варвара
Группа ИУ7-14Б
Лабораторная работа №6
Программа для смены местами минимального положительного и
максимального положительного элементов
"""

from math import inf

# Ввод значений и переменных
num_of_items = input('Введите количество элементов списка: ')
arr = list()

# Защита от хомяков 1 - проверка количества элементов списка
while not num_of_items.isdigit() or num_of_items == '0':
    num_of_items = input('Количество элементов списка должно '
                         'быть целым положительным числом, попробуйте еще раз: ')
num_of_items = int(num_of_items)
# Защита от хомяков 2 - проверка, что все элементы списка - целые числа
for i in range(num_of_items):
    elem = input('Введите элемент: ')
    while elem == '' or not (elem.isdigit() or elem[0] == '-' and elem[1:].isdigit()):
        elem = input('Элемент должен быть целым '
                     'числом, попробуйте еще раз: ')
    arr.append(int(elem))

# Основной алгоритм для смены элементов местами
min_elem = inf
min_index = -1
max_elem = 0
max_index = -1
# Находим минимальный и максимальный элементы вместе с их индексами
for i in range(num_of_items):
    if arr[i] > max_elem and arr[i] > 0:
        max_elem = arr[i]
        max_index = i
    if min_elem > arr[i] > 0:
        min_elem = arr[i]
        min_index = i
# Проверка, что в списке есть хотя бы одно положительное число
if max_elem:
    for i in range(num_of_items):
        if i == max_index:
            arr[i] = min_elem
        if i == min_index:
            arr[i] = max_elem

# Вывод результата
if max_elem:
    if max_elem == min_elem:
        print(
            'В данном списке есть только одно положительное число, '
            'т.е. в данном случае искомые величины совпадают, поменять '
            'их местами не выйдет')
        print(arr)
    else:
        print('Полученный список: ', arr)
else:
    print('В данном списке нет ни одного положительного числа')
