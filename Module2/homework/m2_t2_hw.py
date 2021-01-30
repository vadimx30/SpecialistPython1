# Задача № 2. Проверить, является ли четырехзначное число палиндромом
# Пример:
# Вход: 1221  Выход: 1221 - палиндром
# Вход: 1234  Выход: 1234 - не палиндром

ch = input('Enter N: ')
n = [int(i) for i in ch]
if len(n) == 4:
    c1 = n[:2]
    c2 = n[-1:1:-1]
    if c1 == c2:
        print(f'{ch} is palindrom')
    else:
        print(f'{ch} is not palindrom')
else:
        print('Do nothing.')
