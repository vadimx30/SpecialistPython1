Задача №3
Вход: размер шахматной доски, от 0 до 20
Выход: вывести на экран эту доску с названиями полей.
Пример:
In: 4
Out:
a4 b4 c4 d4
a3 b3 c3 d3
a2 b2 c2 d2
a1 b1 c1 d1


dlsh = int(input('Enter chessmath value: '))
for a  in range(dlsh):
    for b in range(dlsh):
        x = dlsh - a
        y = chr(97+ b)
        print(f'{y}{x}',end = ' ')
    print()
