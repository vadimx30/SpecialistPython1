"""
Используя cmd.exe формируем файл zen.txt
py -m this > zen.txt

Вход: файл в котором записан Zen of Python на английском языке
Выход: словарь-частотник (желательно минусовать предлоги и артикли)
Знаки препинания и апострофы удаляем.
Пример:
out_dict = {'better' : 6,
            'complex': 2,
            'never': 4}
"""

import string as st
from pprint import pprint
a = open('zen.txt', 'r') ## открытый файл
stroki = list(a) ## деление открытого файла по строкам
words = [] ## деление строк по словам
allwords = [] ## общее по словам
f = ''
allwords2 = []
dict_zen = {}
iskl = ['the', 'of', 'by', 'is', 'than', '', 'to', 'a', 'are', 'at']
for i in stroki:
    words = [k for k in i.split()]
    allwords.extend(words)
a.close()
for i in allwords:
    e = list(i)
    for k in e:
        for g in list(st.ascii_letters):
            if g == k:
                f += k
                break
    allwords2.append(f)
    f = ''
for i in allwords2:
    i = i.lower()
    if dict_zen.get(i):
        dict_zen[i] += 1
    else:
        dict_zen[i] = 1
for i in iskl:
    if dict_zen.get(i):
        dict_zen.pop(i)
pprint(dict_zen)
