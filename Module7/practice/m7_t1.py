"""
Написать функцию для сложения двух аргументов, в которую нужно
добавить обработку исключений для случаев сложения str с int, float и bool
"""

import string as st
import random
a = random.randint(0, 20)
b = random.sample(list(st.ascii_letters),1)
c = random.sample([True, False],1)
d = random.random()
e = {1:a, 2:b, 3:c, 4:d}
number1 = e[random.randint(1,4)]
number2 = e[random.randint(1,4)]
print(f'Первый аргумент: {number1}')
print(f'Второй аргумент: {number2}')
try:
    number1 + number2
    print(f'Сумма аргументов: {number1 + number2}')
except TypeError:
    print('Нельзя сложить')
