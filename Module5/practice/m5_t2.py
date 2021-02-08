'''
Задача №2. Шахматная доска
Вход: размер шахматной доски, от 0 до 20
Выход: вывести на экран эту доску, заполняя поля нулями и единицами

Пример:
Вход: 4
Выход:
    0 1 0 1
    1 0 1 0
    0 1 0 1
    1 0 1 0
'''

import func_m5_t2
a = int(input('Введите число от 0 до 20: '))
while a < 0 or a > 20:
    a = int(input('Введите число от 0 до 20: '))
if a == 0:
    print('')
for i in range(a):
    if i % 2:
        print(*func_m5_t2.chet(a))
    else:
        print(*func_m5_t2.nechet(a))
        
# func_m5_t2
def nechet(a: int) -> list:
    """Строка по нечетным"""
    i = 0
    result = []
    while i < a:
        if i % 2:
            result.append(1)
        else:
            result.append(0)
        i += 1
    return result

def chet(a: int) -> list:
    """Строка по четным"""
    i = 0
    result = []
    while i < a:
        if i % 2:
            result.append(0)
        else:
            result.append(1)
        i += 1
    return result
