"""
Используя функцию random.randint(1, 1000) сформировать список
 из 20 элементов и сохранить в файл.
 После этого, считать числа из файла и посчитать среднее арифметическое.
 """
import random
f = 'spisok.rnd'
file = open(f,'w')
for i in range(20):
    char = str(random.randint(1, 1000))+'\n'
    file.write(char)
file.close()


a,ar = 0,0
with open(f) as file:
    for smv in file.readlines():
        j = smv[0:len(smv)-1]
        if str.isdigit(j):
            ar += int(j)
            a += 1
if not(a == 0):
    srd = ar/a
else:
    srd = 0
print(f'{a} Srednee = {srd}')
