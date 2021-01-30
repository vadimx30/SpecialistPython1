"""
Дана строка из двух слов. Поменяйте эти слова местами.
Пример:
In: Hello Python
Out: Python Hello
"""
string = [i for i in input('Enter string: ').split()]
string = string[::-1]
print(*string)
