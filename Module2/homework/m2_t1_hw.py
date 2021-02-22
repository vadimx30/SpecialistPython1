# Задача № 1. Вывести на экран в порядке возрастания три введенных числа
# Пример:
# Вход: 1, 9, 2
# Выход: 1, 2, 9

a = int(input('Введите число a: '))
b = int(input('Введите число b: '))
c = int(input('Введите число c: '))
if a <= b:
    if b <= c:
        print(a, b, c)
    elif a < c:
        print(a, c, b)
    else:
        print(c, a, b)
else:
    if b >= c:
        print(c, b, a)
    elif a < c:
        print(b, a, c)
    else:
        print(b, c, a)
