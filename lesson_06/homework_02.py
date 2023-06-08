# Задача 2
# Определить индексы элементов массива (списка),
# значения которых принадлежат заданному диапазону (т.е. не
# меньше заданного минимума и не больше заданного
# максимума)
# Ввод: [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
# Вывод: [1, 9, 13, 14, 19]

import random

print('----------------------------------')

start = int(input("Введите минимальное значение: "))
finish = int(input("Введите максимальное заначение: "))
list_one = random.sample(range(-10, 11), 20)
print(list_one)

def interval_list (list, start, finish):
    # result = []
    # for i in range(len(list)):
    #     if list[i] > start and list[i] < finish:
    #         result.append(i)
    # сначало        "i"    сам индекс который мы будем записывать, 
    # потом          "for i in range(len(list))"    перебераем эти индесы, 
    # и только потом "if list[i] > start and list[i] < finish"      идет условие 
    result = [i for i in range(len(list)) if list[i] > start and list[i] < finish]
    # НО если надо в проверки сделать ислючение или другие проверки,
    # порядок изменяеться 
    # сначало так же "i"
    # и потом уже спроверки с "ичначе"
    # и последним идет цикл,
    # но всегда первым идет элемент который мы добавляем
    # result = [i if list[i] > start and list[i] < finish else ' ' for i in range(len(list))]

    return result

list_result = []
list_result = interval_list(list_one, start, finish)
print(list_result)

print('----------------------------------')