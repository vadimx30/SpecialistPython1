"""
Дана строка из символов(латинские букы + цифры)
Нужно вывести новой строкой только цифры, если они есть или написать, что их нет.
Пример: 
In: 'antuh1ouou21au3'
Out: 1213
"""
text = (input('enter:'))
list1 = []
list2 = []
for i in text:
    list1.append(i)
for i in list1:
    if (i.isdigit()):
        list2.append(i)
if list2 != []:
    a = ''.join(list2)
    print(a)
else:
    print('Цифр нет')
