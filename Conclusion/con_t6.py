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