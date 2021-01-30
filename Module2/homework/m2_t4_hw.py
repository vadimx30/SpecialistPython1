# Задача №4
# Вход: строка и символ
# Выход: количество вхождений символа в строку.
# Вводим строку до тех пор, пока длина строки
# меньше 5 символов.

lens = 0
while lens <5:
    string = input('Enter string ')
    lens = len(string)
    if lens <5: print('Need 5 chars minimum!')
 
lens = 0
while not lens == 1:
    char = input('enter char ')
    lens = len(char)
    if not lens == 1: print('Need a char!')

qq = 0
for i in string:
    if i == char:
        qq += 1
print(f'Quantity {char} in {string} = {qq}')
