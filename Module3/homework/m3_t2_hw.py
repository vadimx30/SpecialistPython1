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
list1 = []
num = int(input('Введите количество чмсел:'))
for i in range(1, num + 1):
    a = int(input('Введите число:'))
    list1.append(a)
b = min(list1)
list1.sort()
list1.pop(0)
c = min(list1)
print(b, c)
