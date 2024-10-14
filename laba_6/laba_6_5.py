"""
Бондарева Варвара
Группа ИУ7-14Б
Лабораторная работа №6

"""

def isPrime(n):
    if n % 2 == 0 or n == 1:
        return n == 2
    d = 3
    while d * d <= n and n % d != 0:
        d += 2
    return d * d > n

print(isPrime(5))