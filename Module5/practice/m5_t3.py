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

import func_m5_t3
c = int(input('Введите число от 0 до 20: '))
while c < 0 or c > 20:
    c = int(input('Введите число от 0 до 20: '))
if c == 0:
    print('Вы потеряли шахматную доску')
i = 0
while i < c:
    print(*func_m5_t3.stroka(i, c))
    i += 1

# func_m5_t3
import string as st
def stroka(cikl: int, point: int) -> list:
    a = [i for i in st.ascii_lowercase]
    b = [i for i in range(point + 1)]
    result = []
    for i in range(point):
        d = a[i] + str(point - cikl)
        result.append(d)
    return result
