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

z = int(input('Введите количество генерируемых чисел: '))

from random import randint
nums = [randint(1, 100) for _ in range(z)]

print('Последовательность:', *nums)

#сортируем и убираем дубли
nums.sort()
sequence = [nums[0]]
i = 1
j = 0
while i < len(nums):
    if sequence[j] != nums[i]:
        sequence.append(nums[i])
        j += 1
    i += 1

x = sequence[:1]
sequence.pop(0)
y = sequence[:1]

print('Самые малые числа:', *x, 'и', *y)
