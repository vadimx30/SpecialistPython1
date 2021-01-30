# Задача №4
# Вход: строка и символ
# Выход: количество вхождений символа в строку.
# Вводим строку до тех пор, пока длина строки
# меньше 5 символов.

letter = input('Введите символ: ')
text = input('Введите текст: ')
count = 0

while len(text) < 5:
        for i in text:
            if i == letter:
                count += 1
        text = input('Введите текст: ')
else:
        for i in text:
            if i == letter:
                count += 1
        
print(f'Накопленное количество вхождений символа "{letter}" в строку: {count}')
