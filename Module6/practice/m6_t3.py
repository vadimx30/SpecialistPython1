"""
Используя функцию random.randint(1, 1000) сформировать список
 из 20 элементов и сохранить в файл.
 После этого, считать числа из файла и посчитать среднее арифметическое.
 """

from random import randint

Z = 20

with open('m6_t3_MIV.txt', 'w') as f:
    for _ in range(Z):
        f.write(str(randint(1, 1000)) + '\n')

result = []
with open('m6_t3_MIV.txt', 'r') as f:
    for line in f:
        result.append(int(line.strip('\n')))
print('Среднее значение сгенерированных'
      'чисел: {0:.2f}'.format(sum(result) / len(result)))
