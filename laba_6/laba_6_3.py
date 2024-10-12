"""
Бондарева Варвара
Группа ИУ7-14Б
Лабораторная работа №6
Программа для нахождения k-ого экстремума в списке
"""

# Ввод значений и переменных
num_of_items = input('Введите количество элементов списка: ')
k = input('Введите номер искомого экстремума: ')
arr = list()
extremes_col = 0
result = 0
arr_is_correct = False

# Защита от хомяков 1 - проверка количества элементов списка
while not num_of_items.isdigit():
    num_of_items = input('Количество элементов списка должно '
                         'быть целым положительным числом, попробуйте еще раз: ')
num_of_items = int(num_of_items)
# Защита от хомяков 2 - проверка номера экстремума
while not k.isdigit():
    k = input('k должно быть целым положительным '
              'числом, попробуйте еще раз: ')
k = int(k)
# Защита от хомяков 3 - проверка, что все элементы списка - целые числа
for i in range(num_of_items):
    elem = input('Введите элемент: ')
    while not (elem.isdigit() or elem[0] == '-' and elem[1:].isdigit()):
        elem = input('Элемент должен быть целым '
                     'числом, попробуйте еще раз: ')
    arr.append(int(elem))

# Нахождение экстремумов списка
for i in range(1, num_of_items - 1):
    if ((arr[i - 1] < arr[i] and arr[i] > arr[i + 1]) or
            ((arr[i - 1] > arr[i]) and arr[i] < arr[i + 1])):
        extremes_col += 1
    if extremes_col == k:
        result = arr[i]
        break

# Блок вывода значений
if num_of_items < 3:
    print('Недостаточное количество элементов для поиска экстремума')
else:
    if extremes_col == k:
        print(f'Искомый экстремум: {result}')
    else:
        print('Искомый экстремум не был найден')
