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


string = [i for i in input('Enter string: ')]
for item in string:
    print(item+':',string.count(item))
