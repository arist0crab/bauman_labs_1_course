"""
Бондарева Варвара
Группа ИУ7-14Б
Лабораторная работа №7
Программа, добавляющая после каждого четного
элемента целочисленного списка его удвоенное значение
Вариант 2
"""

# Ввод значений и переменных
num_of_items = input('Введите количество элементов списка: ')
arr = list()
num_of_even = 0

# Защита от хомяков 1 - проверка количества элементов списка
while not num_of_items.isdigit() or num_of_items == '0':
    num_of_items = input('Количество элементов списка должно '
                         'быть целым положительным числом, попробуйте еще раз: ')
num_of_items = int(num_of_items)
# Защита от хомяков 2 - проверка, что все элементы списка - целые числа
for i in range(num_of_items):
    elem = input('Введите элемент: ')
    while elem == '' or not elem.lstrip('-').isdigit():
        elem = input('Элемент должен быть целым '
                     'числом, попробуйте еще раз: ')
    arr.append(elem:=int(elem))
    num_of_even += elem % 2 == 0

# Основной алгоритм
# Добавляем в конец списка столько нулей, сколько у нас четных чисел
arr += [0] * num_of_even
current_index = num_of_items - 1
# Основной цикл перестановки чисел
while num_of_even > 0:
    if arr[current_index] % 2 == 0:
        arr[current_index + num_of_even] = arr[current_index] * 2
        num_of_even -= 1
    arr[current_index + num_of_even] = arr[current_index]
    current_index -= 1

# Вывод полученного списка
print(f'Полученный список: {arr}')
