# Задача 2
# Напишите рекурсивную функцию sum(a, b),
# возвращающую сумму двух целых неотрицательных чисел. Из
# всех арифметических операций допускаются только +1 и -1.
# Также нельзя использовать циклы.
# 2 2
# 4

print('----------------------------------')

numbA = int(input("Введите чило А: "))
numbB = int(input("Введите чило B: "))

def Sum(a, b):
    if a == 0:
        return b
    elif b == 0:
        return a
    else:
        return Sum(a - 1, b + 1)
    
result = Sum(numbA, numbB)
print("Сумма:", result)

print('----------------------------------')