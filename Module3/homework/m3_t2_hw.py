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
