# Задача №4
# В заданной строке найти количество вхождений символа 'a'


string = input('Enter string: ')
Q = 0
for i in string:
    if i == 'a':
        Q+=1
print(f'Quantity a in {string} = {Q}')
