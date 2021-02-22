""" 3. Написать функцию, используя набор букв из модуля string(string.ascii_lowercase),
    которая расшифрует строку. Каждая буква - это две цифры.
    Отчет с 00 -> 'a' и до 25 -> 'z', 26 - это пробел, он не входит в набор букв
    Вход: строка из цифр. Выход: Текст.
    Проверка работы функции выполняется через вторую строку.
"""
code = '070411111426152419071413'

import string
code = '070411111426152419071413'
code1 = list(code)
a = list(string.ascii_lowercase)
a.append(' ')
b = []
k = 0
m = ''
while k <= 26:
    if k < 10:
        m = '0' + str(k)
        b.append(m)
    else:
        m = str(k)
        b.append(m)
    k += 1
dicti = {}
for i in range(27):
    dicti[b[i]] = a[i]
c = 0
i = 0
result = ''
while i < len(code):
    c = code[i] + code[i + 1]
    i += 2
    result += dicti[c]
print(result)
