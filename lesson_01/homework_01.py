# Задача 1:
# Найдите сумму цифр трехзначного числа.
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0) |

print('----------------------------------')
numb = input("Введите трех значное число ")

sum = int(numb[0]) + int(numb[1]) + int(numb[2])

print()
print(f"Сумма цифр терхзначего числа = {sum}")
print('----------------------------------')