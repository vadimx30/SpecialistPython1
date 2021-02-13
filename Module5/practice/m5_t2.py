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



def xor_c(c):
    if c == 1:
        c = 0
    else:
        c = 1
    return c
    
dlsh = int(input('Enter chessmath value: '))
c = 1
for _ in range(dlsh):
    d = xor_c(c)
    for _ in range(dlsh):
        c = xor_c(c)
        print(f'{c}',end = ' ')
    print()
    c = d
