"""
Бондарева Варвара
Группа ИУ7-14Б
Лабораторная работа №6
Программа для удаления элемента с заданным индексом алгоритмически
"""

# Ввод значений и переменных
elem_index = input('Введите индекс элемента, который хотите удалить: ')
num_of_items = input('Введите количество элементов списка: ')
arr = list()
ei_right_1, ei_right_2 = False, False

# Глобальная защита от хомяков
# Защита от хомяков - проверка количества элементов списка
while not num_of_items.isdigit() or num_of_items == '0':
    num_of_items = input('Количество элементов списка должно '
                         'быть целым положительным числом, попробуйте еще раз: ')
num_of_items = int(num_of_items)
# Защита от хомяков - проверка, что все элементы списка - целые числа
for i in range(num_of_items):
    arr_elem = input('Введите элемент: ')
    while not (arr_elem.isdigit() or arr_elem[0] == '-' and arr_elem[1:].isdigit()):
        arr_elem = input('Элемент должен быть целым '
                     'числом, попробуйте еще раз: ')
    arr.append(int(arr_elem))
# Защита от хомяков следующих параметров:
# 1) Индекс должен быть целым числом
# 2) Индекс должен быть в диапазоне списка
while (not ei_right_1 or not ei_right_2) and arr:
    # Защита от хомяков 1, смотрим, ввел ли пользователь индекс корректно
    ei_right_1 = elem_index.isdigit() or elem_index[0] == '-' and elem_index[1:].isdigit()
    while not ei_right_1:
        elem_index = input('Вы неправильно указали индекс элемента. '
                           'Попробуйте еще раз: ')
        ei_right_1 = (elem_index.isdigit()
                      or elem_index[0] == '-' and elem_index[1:].isdigit())
    elem_index = int(elem_index)
    ei_right_2 = ((0 <= elem_index < len(arr)) or
                  (elem_index < 0 and -1 >= elem_index >= -len(arr)))
    if not ei_right_2:
        elem_index = input('Введенный индекс выходит за '
                           'диапазон списка, давайте другое: ')

# Алгоритмическое добавление элемента в список по индексу
new_arr = arr.copy()
elem_index = len(arr) - abs(elem_index) if elem_index < 0 else elem_index
for i in range(elem_index + 1, len(arr)):
    arr[i - 1] = arr[i]
arr.pop(-1)

# Вывод полученного списка
print(f'Полученный список: {arr}')
new_arr.pop(elem_index)
print('Результат работы insert в аналогичных условиях: ', arr)
