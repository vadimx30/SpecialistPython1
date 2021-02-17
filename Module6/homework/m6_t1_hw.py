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

result = []
with open('zen.txt', 'r') as f:
    for line in f:
        result.append(str(line.strip('\n')).split())

start_str = str(list((i for sublist in result for i in sublist)))

for i in st.punctuation:
    start_str = start_str.replace(i,'')

start_list = list(start_str.split())

finish_list = []
black_list = ['of', 'by', 'The', 'is', 'than', 'arent',
              'to', 'the', 'youre', 'and', 'may', 'not',
              'be', 'at', 'If', 'its', 'a', 'are', 'In',
              'There']
for i in start_list:
    if i not in black_list:
        finish_list.append(i)

unique_list = list(set(finish_list))
finish_dict = {i:finish_list.count(i) for i in unique_list}

list_keys = list(finish_dict.keys())
list_keys.sort()

pprint(finish_dict)

with open('m6_t1_hw_MIV.txt', 'w') as f:
    for i in list_keys:
        print(i, ':', finish_dict[i], file=f)
