# Задача 2
# Требуется найти в массиве A[1..N] самый близкий по
# величине элемент к заданному числу X. Пользователь в первой строке
# вводит натуральное число N – количество элементов в массиве. В
# последующих строках записаны N целых чисел Ai
# . Последняя строка
# содержит число X
# 5
# 1 2 3 4 5
# 6
# -> 5

print('----------------------------------')

n = int(input("Введите длинну массива "))
list = [int(input(f"вветиде {i} число ")) for i in range(n)]
# list = [1,2,3,4,5]
print(list)
x = int(input("Введиет число что бы найти самый близкий по величине элемент к заданному числу "))

closest = []
min_diff = 1
for item in list:
        diff = abs(item - x) 
        # print(f"{item} != {x} and {diff} < {min_diff}")
        if item != x and diff == min_diff:
            min_diff = diff
            closest.append(item)

print(f"Последнее ближайщее число/числа к числу {x} = {closest}")

print('----------------------------------')