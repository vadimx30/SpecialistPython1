"""
Дана строка из символов(латинские букы + цифры)
Нужно вывести новой строкой только цифры, если они есть или написать, что их нет.
Пример: 
In: 'antuh1ouou21au3'
Out: 1213
"""

text = input('Введите текст: ')
lst = [_ for _ in text]
DIGITS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
text_numbers=list()

for _ in lst:
    if _ in DIGITS:
        text_numbers.append(_)
if text_numbers == []:
    print('Чисел нет')
else:
    print(f'Введенные числа: {"".join(text_numbers)}')
