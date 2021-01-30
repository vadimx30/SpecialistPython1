string = input('Введите строку: ')
s = input('Введите символ: ')
h = 0

while len(string) < 5:
    print ('Длина строки должна быть больше 5 символов')
    string = input('Введите строку: ')
else:
    for x in string:
        if x == s:
             h += 1
print(f'Количество вхождений символа в строку: {h}') 
