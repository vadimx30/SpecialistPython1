""" 3. Написать функцию, используя набор букв из модуля string(string.ascii_lowercase),
    которая расшифрует строку. Каждая буква - это две цифры.
    Отчет с 00 -> 'a' и до 25 -> 'z', 26 - это пробел, он не входит в набор букв
    Вход: строка из цифр. Выход: Текст.
    Проверка работы функции выполняется через вторую строку.
"""
code = '070411111426152419071413'


def decodestring(code):
    import string
    straii = string.ascii_lowercase+' '
    i = 0
    strvyh = ''
    while i < len(code):
        sim = int(code[i:i+2])
        if sim > len(straii):
            encode = '#'
        else:
            encode = straii[sim]
        i +=2
        strvyh += encode
    return strvyh
    
    
print(decodestring(code))
