'''
Даны  два  кортежа A и B, каждый  кортеж  состоит  из  N элементов.
Написать функцию для подсчета количества  тех  элементов  кортежа A,  для которых:
1) Ai > Bi
2) Ai = Bi
3) Ai < Bi
'''

import func
a  = tuple(map(int, input('Введите первый котреж чисел: ').split()))
b = tuple(map(int, input('Введите второй котреж чисел: ').split()))
if len(a) != len(b):
    print('количество символов разное')
    while len(b) != len(a):
        b = tuple(input(f'Введите второй кортеж из {len(a)} чисел: '))
bl, m, r = func.poisk(a, b)
print(f'Ai > Bi:  {bl}')
print(f'Ai = Bi: {r}')
print(f'Ai < Bi: {m}')

#func
def poisk(a: tuple, b:tuple) -> tuple:
    """poisk neravenstv dvuh kortezhey"""
    bol = 0
    men = 0
    rav = 0
    for i in range(len(a)):
        if a[i]  > b[i]:
            bol += 1
        elif a[i] < b[i]:
            men += 1
        else:
            rav += 1
    return bol, men, rav
