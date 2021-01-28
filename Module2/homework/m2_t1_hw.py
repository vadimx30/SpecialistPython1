# Задача № 1. Вывести на экран в порядке возрастания три введенных числа
# Пример:
# Вход: 1, 9, 2
# Выход: 1, 2, 9

if a <= b <= c:
    print(a, b, c)
elif a <= c <= b:
    print(a, c, b)
    
elif b <= a <= c:
    print(b, a, c)
elif b <= c <= a:
    print(b, c, a)
    
elif c <= a <= b:
    print(c, a, b)
else:
    print(c, b, a)
