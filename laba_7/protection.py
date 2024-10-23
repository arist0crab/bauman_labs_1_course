"""
Бондарева Варвара
Группа ИУ7-14Б
Лабораторная работа №7
Программа для переворачивания второй части списка
Защита
"""

# Ввод значений и переменных
num_of_items = input('Введите количество элементов списка: ')
arr = list()

# Защита от хомяков - проверка количества элементов списка
while not num_of_items.isdigit() or num_of_items == '0':
    num_of_items = input('Количество элементов списка должно '
                         'быть целым положительным числом, попробуйте еще раз: ')
num_of_items = int(num_of_items)

# Создание списка строк
arr = [input('>> ') for i in range(num_of_items)]

col = len(arr) // 2 - 1
for i in range(len(arr) // 2 + len(arr) % 2, len(arr) - len(arr) // 4):
    arr[i], arr[i + col] = arr[i + col], arr[i]
    col -= 2

print(arr)