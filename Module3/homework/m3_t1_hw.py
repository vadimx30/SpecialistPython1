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

a = [i for i in input('Введите несколько чисел через пробел:').split()]
for i in range(len(a)):
    a[i] = int(a[i])
k = 1
b = []
while k < len(a):
    c = a[k] - a[k - 1]
    b.append(c)
    k += 1
d = []
g = 0
while g < len(b):
    if b[g] == 0:
        g += 1
    else:
        d = b.copy()
        d.insert(0, b[g])
        break  
else:
    print('CONSTANT')
e = 1
if d[0] > 0:
    result = 'ASCENDING'
    while e < len(d):
        if d[e] == 0:
            result = 'WEAKLY ASCENDING'
        elif d[e] < 0:
            result = 'RANDOM'
            break
        e += 1
else:
    result = 'DESCENDING'
    while e < len(d):
        if d[e] == 0:
            result = 'WEAKLY DESCENDING'
        elif d[e] > 0:
            result = 'RANDOM'
            break
        e += 1
print(result)
