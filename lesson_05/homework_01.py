# Задача 1
# Напишите программу, которая на вход принимает
# два числа A и B, и возводит число А в целую степень B с
# помощью рекурсии.
# A = 3; B = 5 -> 243 (3⁵)
# A = 2; B = 3 -> 8

print('----------------------------------')

numbA = int(input("Введите чило А: "))
numbB = int(input("Введите чило B: "))

def PowerRecursive(a, b):
    if b == 0:
        return 1
    elif b < 0:
        return 1 / PowerRecursive(a, -b)
    else:
        return a * PowerRecursive(a, b - 1)
    
result = PowerRecursive(numbA, numbB)
print(f"{numbA} в степени {numbB} = {result}")

print('----------------------------------')