"""
Программа получает на вход последовательность целых чисел N(1-10).
Вам нужно определить вид последовательности:
 - возрастающая
 - убывающая
 - случайная
 - постоянная
В качестве ответа следуют выдать прописными латинскими буквами тип последовательности:
1. ASCENDING (строго возрастающая)
2. WEAKLY ASCENDING (нестрого возрастающая, то есть неубывающая)
3. DESCENDING (строго убывающая)
4. WEAKLY DESCENDING (нестрого убывающая, то есть невозрастающая)
5. CONSTANT (постоянная)
7. RANDOM (случайная)
Примеры входных и выходных данных:
In: 9 4 2 -1  Out: DESCENDING
In: 3 8 8 11  Out: WEAKLY ASCENDING
In: 2 -1 7    Out: RANDOM
In: 5 5 5 5   Out: CONSTANT
"""


c = []
result = 'NULL'
i = 0
while i < 10:
    ch = int(input('Enter ['+str(i)+']: '))
    c.append(ch)
    if i>0:
       if c[i] == c[i-1]:
           if result == 'DESCENDING':
               result = 'WEAKLY DESCENDING'
           if result == 'ASCENDING':
               result = 'WEAKLY ASCENDING'
           if result == 'NULL':
               result = 'CONSTANT'
       if c[i] < c[i-1]:
           if result == 'NULL':
               result = 'DESCENDING'
           if result == 'CONSTANT':
               result = 'WEAKLY DESCENDING'
           if result == 'ASCENDING' or result == 'WEAKLY ASCENDING':
               result = 'RANDOM'   
       if c[i] > c[i-1]:
           if result == 'NULL':
               result = 'ASCENDING'
           if result == 'CONSTANT':
               result = 'WEAKLY ASCENDING'
           if result == 'DESCENDING' or result == 'WEAKLY DESCENDING':
               result = 'RANDOM'   
    i += 1
print(*c,' is '+result)
