"""
Бондарева Варвара
Группа ИУ7-14Б
Лабораторная работа №7
Программа, которая ищет элемент с наибольшим числом
английских согласных букв в списке строк
Вариант 2
"""

# Ввод значений и переменных
num_of_items = input('Введите количество элементов списка: ')

# Защита от хомяков - проверка количества элементов списка
while not num_of_items.isdigit() or num_of_items == '0':
    num_of_items = input('Количество элементов списка должно '
                         'быть целым положительным числом, попробуйте еще раз: ')
num_of_items = int(num_of_items)

# Создание списка строк
arr = [input('>> ') for i in range(num_of_items)]

# Основной алгоритм
max_consonants = 0
max_index = -1
# Делаем проход по каждой строке списка
for elem in range(num_of_items):
    current_consonants = 0
    # Делаем проход по каждой букве строки
    for letter in arr[elem].lower():
        current_consonants += letter in 'qwrtpsdfghjklzxcvbnm'
    # Если в текущей строке больше согласных английских букв, то запоминаем ее
    if current_consonants > max_consonants:
        max_consonants = current_consonants
        max_index = elem

# Вывод результата
if max_index >= 0:
    print(f'Найденный элемент: {arr[max_index]}')
else:
    print('Ни в одной строке списка не нашлось согласных английских букв')
