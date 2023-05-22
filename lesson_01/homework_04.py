# Задача 3:
# Требуется определить, можно ли от шоколадки размером n × m долек 
# отломить k долек, если разрешается сделать один разлом 
# по прямой между дольками (то есть разломить шоколадку на два прямоугольника).
# 3 2 4 -> yes
# 3 2 1 -> no

print('----------------------------------')
x = int((input("Введите количество шоколадных долек по горизонтали ")))
y = int((input("Введите количество шоколадных долек по вертикали ")))
count = int((input("Введите сколько кусочков хотите отломить ")))

# находим максимальное количество плиток
max = x * y

# находим минимальную кратность отломов
if x > y:
    min = y
else:
    min = x

# если желаемое число делиться на кратность 
# без остатка то можно отломить такой кусок
if bool(count % min):
    result = 'нельзя'
else:
    result = 'можно'

print()
print(f"Школдака {x} x {y} плиток, {result} отломить кусочек из {count} плиток")
print('----------------------------------')