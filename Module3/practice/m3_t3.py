"""
Дана строку. Необходимо посчитать количество вхождений каждого символа.
Пример:
In: Hello, Python1
Out: 
H: 1
e: 1
l: 2
o: 2
,: 1
P: 1
y: 1
t: 1
n: 1
1: 1
"""

a = [i for i in input('Введите строку: ')]
print(a)
i = 0
b = []
while i < len(a):
    print('Количество вхождений символа',a[i],'=', a.count(a[i]))
    for k in range(len(a)):
        if a[k] != a[i]:
            b.append(a[k])
    a = b.copy()
    b.clear()
