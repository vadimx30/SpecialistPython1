""" 3. Написать функцию, используя набор букв из модуля string(string.ascii_lowercase),
    которая расшифрует строку. Каждая буква - это две цифры.
    Отчет с 00 -> 'a' и до 25 -> 'z', 26 - это пробел, он не входит в набор букв
    Вход: строка из цифр. Выход: Текст.
    Проверка работы функции выполняется через вторую строку.
"""
code = '070411111426152419071413'

import string as st

n = 2
lst = [code[i:i+n] for i in range(0, len(code), n)]


result = []
try:
    for i in lst:
        result.append(st.ascii_lowercase[int(i)])
except IndexError:
    result.append(' ')
    for i in lst[6:]:
        result.append(st.ascii_lowercase[int(i)])
finally:
    print(''.join(result))
