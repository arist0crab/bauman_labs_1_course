"""
Бондарева Варвара
Группа ИУ7-14Б
Лабораторная работа №6
Программа для добавления элемента по индексу в заданное место списка (алгоритмически)
"""

# Ввод значений и переменных
print('Сейчас мы будем создавать список')
arr = input('Для этого введите элементы в строку через пробел: ').split()
elem = input('Введите новый элемент: ')
elem_index = input('Введите индекс, на который нужно вставить элемент. '
                   'Индекс должен быть ЦЕЛЫМ числом: ')
ei_right_1, ei_right_2 = False, False

# Глобальная защита от хомяков по двум параметрам
# 1) Индекс должен быть целым числом
# 2) Индекс должен быть в диапазоне списка
while not ei_right_1 or not ei_right_2:
    # Защита от хомяков 1, смотрим, ввел ли пользователь индекс корректно
    ei_right_1 = elem_index.isdigit() or elem_index[0] == '-' and elem_index[1:].isdigit()
    while not ei_right_1:
        elem_index = input('Вы неправильно указали индекс элемента. '
                           'Попробуйте еще раз: ')
        ei_right_1 = (elem_index.isdigit()
                      or elem_index[0] == '-' and elem_index[1:].isdigit())
    elem_index = int(elem_index)
    # Защита от хомяков 2, смотрим, не выходит ли индекс за пределы данного списка
    ei_right_2 = ((0 <= elem_index <= len(arr)) or
                  (elem_index < 0 and -1 >= elem_index >= -len(arr)))
    if not ei_right_2:
        elem_index = input('Введенное число выходит за '
                           'диапазон списка, давайте другое: ')

# Алгоритмическое добавление элемента в список по индексу
new_arr = arr.copy()
elem_index = len(arr) - abs(elem_index) if elem_index < 0 else elem_index
arr.append('lol')
for i in range(len(arr) - 1, elem_index, -1):
    arr[i] = arr[i - 1]
arr[elem_index] = elem

# Вывод полученного списка
print(f'Полученный список: {arr}')
new_arr.insert(elem_index, 'HERE')
print('Результат работы insert в аналогичных условиях: ', arr)
