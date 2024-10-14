"""
Бондарева Варвара
Группа ИУ7-14Б
Лабораторная работа №6
Программа для нахождения наиболее длинной непрерывной
убывающей последовательности простых чисел
"""

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

# Основной алгоритм поиска наибольшей последовательности
current_length = 0
max_length = 0
current_start_index = -1
max_start_index = -1
previous = arr[0]
# Проверяем, простой ли первый элемент
if arr[0] <= 0:
    previous_is_simple = False
elif arr[0] % 2 == 0 or arr[0] == 1:
    previous_is_simple = arr[0] == 2
else:
    d = 3
    while d * d <= arr[0] and arr[0] % d != 0:
        d += 2
    previous_is_simple = d * d > arr[0]
if previous_is_simple:
    current_length += 1
    current_start_index = 0
for i in range(1, num_of_items):
    # Проверяем, простой ли элемент
    if arr[i] <= 0:
        current_is_simple = False
    elif arr[i] % 2 == 0 or arr[i] == 1:
        current_is_simple = arr[i] == 2
    else:
        d = 3
        while d * d <= arr[i] and arr[i] % d != 0:
            d += 2
        current_is_simple = d * d > arr[i]
    if current_is_simple and arr[i] < previous and previous_is_simple:
        current_length += 1
        previous_is_simple = True
    else:
        if max_length < current_length:
            max_length = current_length
            max_start_index = current_start_index
        if current_is_simple:
            current_start_index = i
            current_length = 1
            previous_is_simple = True
        else:
            previous_is_simple = False
            current_length = 0
    previous = arr[i]
if max_length < current_length:
    max_length = current_length
    max_start_index = current_start_index

# Вывод результатов на печать
if max_start_index >= 0:
    print('Наиболее длинная непрерывная убывающая последовательность простых чисел: ',
          arr[max_start_index:max_start_index + max_length])
else:
    print('В данном списке не обнаружено искомых последовательностей')
