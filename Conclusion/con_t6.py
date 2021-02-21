""" 6.Прочитать файл presents.txt. В нем числа - стоимости подарков.
    Вывести на экран список покупок, общую сумму, 2 самые дорогие покупки.
"""
from random import randint
from random import seed
seed(777)

with open('presents.txt', 'w') as file:
    for item in range(11):
        end_flag = ' ' if randint(0, 1) else '\n'
        print(round(randint(10, 1000) / randint(2, 10), 2), end=end_flag, file=file)

''' Ваш код'''

with open('presents.txt', 'r') as file:
    d =file.readlines()
pokupki = []
index = 0
for i in d:
    pokupka = i.split()
    ipokupka = [float(i) for i in pokupka]
    for st in ipokupka:
        print(f'pokupka {index+1}  st = {st}')
        index += 1
        pokupki.append(st)
pokupki.sort()
last = pokupki[len(pokupki)-1]
pred = pokupki[len(pokupki)-2]
print(f'maximum pokupki = {last} and {pred}')
