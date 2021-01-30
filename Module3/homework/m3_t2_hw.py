"""
Дана последовательность из N чисел. Найти в ней два самых маленьких числа.
Последовательность можно сформировать с помощью функции randint()
Вариант 1.
from random import randint
nums = []
for _ in range(10):
    nums.append(randint(1, 100))
    
Вариант 2.
from random import randint
res = [randint(1, 100) for _ in range(10)]
"""


from random import randint
N = int(input('Enter N:'))
res = [randint(1, 100) for _ in range(N)]
ch1 = ''
ch2 = ''
for i in res:
    if ch1 == '': #First
        ch1 = i
    else:
        if i < ch1:
            ch2 = ch1
            ch1 = i
        else:
            if ch2 == '':
                ch2 = i
            else:
                if i < ch2:
                    ch2 = i
print(res)
print(f'Two minimum is {ch1} and {ch2}')
