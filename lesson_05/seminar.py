# Последовательностью Фибоначчи называется
# последовательность чисел a0, a1, ..., an, ..., где 
# a0 = 0, a1 = 1, ak = ak-1 + ak-2 (k > 1).
# Требуется найти N-е число Фибоначчи
# Input: 7
# Output: 21
# Задание необходимо решать через рекурсию

# def fibonacci_sequence(n):
#     sequence = []
#     for i in range(n):
#         sequence.append(fibonacci(i))
#     return sequence

# def fibonacci(n):
#     if n <= 0:
#         return 0
#     elif n == 1:
#         return 1
#     else:
#         return fibonacci(n - 1) + fibonacci(n - 2)

# num = int(input("Введите длину последовательности Фибоначчи: "))
# sequence = fibonacci_sequence(num)

# print("Последовательность Фибоначчи:", sequence)


# Хакер Василий получил доступ к классному журналу и
# хочет заменить все свои минимальные оценки на
# максимальные. Напишите программу, которая
# заменяет оценки Василия, но наоборот: все
# максимальные – на минимальные.
# Input: 5 -> 1 3 3 3 4
# Output: 1 3 3 3 1

# count = int(input("Введите количество оценок: "))
# list = [int(input()) for x in range(count)]

# def ReturnRating(arr):
#     for x in range(len(arr)):
#         if arr[x] > 3:
#             arr[x] = 1

# ReturnRating(list)
# print(list)

# Напишите функцию, которая принимает одно число и
# проверяет, является ли оно простым
# Напоминание: Простое число - это число, которое
# имеет 2 делителя: 1 и n(само число)
# Input: 5
# Output: yes

# numb = int(input("Введите число: "))

# def PrimeNumber(n):
#     k = 0
#     for i in range(2, n // 2+1):
#         if (n % i == 0):
#             k = k+1
#     if (k <= 0):
#         print("Число простое")
#     else:
#         print("Число не является простым")

# PrimeNumber(numb)

# Дано натуральное число N и
# последовательность из N элементов.
# Требуется вывести эту последовательность в
# обратном порядке.
# Примечание. В программе запрещается
# объявлять массивы и использовать циклы
# (даже для ввода и вывода).
# Input: 2 -> 3 4
# Output: 4 3

# def nums_mirror(n):
#     temp = input("Р’РІРµРґРёС‚Рµ С‡РёСЃР»Рѕ: ")
#     if n == 1:
#         return temp
#     return nums_mirror(n - 1) + temp


# print(nums_mirror(5))