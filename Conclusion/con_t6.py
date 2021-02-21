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

lst = []
with open('presents.txt', 'r') as f:
    for line in f.readlines():
        lst.append((line.strip('\n')))

result = ' '.join(lst)

result = result.split()
print(f'Список покупок: {", ".join(result)}')

float_lst = []
for i in result:
    float_lst.append(float(i))

sum_res = sum(float_lst)
print(f'Сумма: {sum_res}')


max_1 = max(float_lst)
float_lst.remove(max_1)
max_2 = max(float_lst)
print(f'Две самые дорогие покупки: {max_1}, {max_2}')
