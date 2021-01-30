str = input('Введите символы: ')
letter = 'a'
count = 0
while str:
    if str[0] == letter:
        count += 1
    str = str[1:]
    
print('Колличество  символо, равных "a": ', count)
