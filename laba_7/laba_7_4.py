"""
Бондарева Варвара
Группа ИУ7-14Б
Лабораторная работа №7
Программа для замены двух подряд идущих
цифр на последнюю букву их суммы
Вариант 6
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
    if len(elem) == 1 and elem.isdigit():
        elem = int(elem)
    arr.append(elem)

# Основной цикл
# Проходимся по всем элементам списка, складываем два подходящих значения,
# следующее после этого значения обращаем в None, чтобы потом удалить
for i in range(num_of_items - 1):
    if arr[i] is None:
        continue
    if type(arr[i]) is int and type(arr[i + 1]) is int:
        arr[i] += arr[i + 1]
        arr[i] %= 10
        arr[i + 1] = None
# Удаляем все значение None (тот же алгоритм, что и в первом задании)
insert_index = 0
for elem in arr:
    # Проверяем, подходит ли элемент под условие
    if elem is not None:
        arr[insert_index] = elem
        insert_index += 1
arr = arr[:insert_index]

# Вывод полученного списка
print(f'Полученный список: {arr}')
