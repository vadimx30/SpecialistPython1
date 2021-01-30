# Задача №4
# В заданной строке найти количество вхождений символа 'a'
string = input('Enter string: ')
q = 0
for i in string:
    if i == 'a':
        q + = 1
print(f'Quantity a in {string} = {q}')
