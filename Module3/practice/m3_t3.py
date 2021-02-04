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

text = input('Введите текст: ')
lst = [_ for _ in text]
used_letters = list()
lst.remove(' ')

for _ in lst:
    if _ in used_letters:
        continue
    else:
        print(_, ':', lst.count(_))
        used_letters.append(_)
