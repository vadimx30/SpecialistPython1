"""
Дана строка из символов(латинские букы + цифры)
Нужно вывести новой строкой только цифры, если они есть или написать, что их нет.
Пример: 
In: 'antuh1ouou21au3'
Out: 1213
"""


string = input('Enter string: ')
result = [item for item in string if item >= '0' and item <='9']
if result:
    for i in result:
        print(i,end='')
else:
    print('No numeric')
