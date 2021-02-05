"""
Дана последовательность символов, не более 9 символов,имеющая следующий вид:
p1*p2*p3*....*pn, где pi - цифра. Вычислите значение выражения.
Пример:
In: 5*3*2
Out: 30
"""

LIMIT = 9
formula = input('Введите последовательность символов'
                ' вида p1*p2*p3*....*pn, где pi - цифра'
                '(не более 9 символов): ')
while len(formula) > LIMIT:
    formula = input('Введите последовательность символов'
                    ' вида p1*p2*p3*....*pn, где pi - цифра'
                    '(не более 9 символов): ')

lst= formula.split('*')
numbers = list(map(int, lst))

import math
result = math.prod(numbers)


print(f'{"".join(formula)} = {result}')
print(*formula,' = ', result, sep='')
print('{} = {}'.format(formula, result))
