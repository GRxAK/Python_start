
# # Дан список чисел. Определите, сколько в нем
# # встречается различных чисел.
# # Input: [1, 1, 2, 0, -1, 3, 4, 4]
# # Output: 6

# list = [1, 1, 2, 0, -1, 3, 4, 4]
# sp = {}
# for el in list:
#     if el not in sp:
#         sp[el] = 1
#     else:
#         sp[el] += 1
# print(sp)


# # Дана последовательность из N целых чисел и число
# # K. Необходимо сдвинуть всю последовательность
# # (сдвиг - циклический) на K элементов вправо, K –
# # положительное число.

# k = 3
# x = [1, 2, 3, 4, 5]
# y = x[k:] + x[:k]
# print(y)


# # Напишите программу для печати всех уникальных
# # значений в словаре.
# # Input: [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"},
# # {"VI": "S005"}, {"VII": " S005 "}, {" V ":" S009 "}, {" VIII
# # ":" S007 "}]
# # Output: {'S005', 'S002', 'S007', 'S001', 'S009'}
# # Примечание: Список словарей задан изначально.
# # Пользователь его не вводит

# dictionary = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII": "S005"}, {" V ":"S009"}, {" VIII":"S007"}]
# unique = set()
# for item in dictionary:
#     unique.add(*item.values())
# print(unique)


# Дан массив, состоящий из целых чисел. Напишите
# программу, которая подсчитает количество
# элементов массива, больших предыдущего (элемента
# с предыдущим номером)
# Input: [0, -1, 5, 2, 3]
# Output: 2 (-1 < 5, 2 < 3)
# Примечание: Пользователь может вводить значения
# списка или список задан изначально.

numbers = [0, -1, 5, 2, 3]
count = 0
for i in range(0, len(numbers) - 1):
    if numbers[i + 1] > numbers[i]:
        count += 1
print(count)