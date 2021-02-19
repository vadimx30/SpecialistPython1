"""
Используя функцию random.randint(1, 1000) сформировать список
 из 20 элементов и сохранить в файл.
 После этого, считать числа из файла и посчитать среднее арифметическое.
 """

from random import randint
elem = [randint(1, 1000) for _ in range(20)]
resultwrite = open('result.txt', 'w')
for i in elem:
    i = str(i) + '\n'
    resultwrite.write(i)
resultwrite.close()
srarifm = 0
resultread = open('result.txt', 'r')
summ = [k for k in resultread.readlines()]
for m in summ:
    m = int(m)
    srarifm += m
resultread.close()
srarifm = srarifm / 20
print(f'Среднее арифметическое = {srarifm}')
