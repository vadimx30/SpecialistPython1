"""
Используя функцию random.randint(1, 1000) сформировать список
 из 20 элементов и сохранить в файл.
 После этого, считать числа из файла и посчитать среднее арифметическое.
 """
import statistics
from random import randint
x = 20
with open('m6_t3.txt', 'w') as f:
    for _ in range(x):
        f.write(str(randint(1, 1000)) + '\n')

with open('m6_t3.txt', 'r') as f:
    l = [int(line.strip()) for line in f]

m = statistics.mean(l)
print(m)
