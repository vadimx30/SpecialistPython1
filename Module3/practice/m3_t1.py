"""
Дана строка из двух слов. Поменяйте эти слова местами.
Пример:
In: Hello Python
Out: Python Hello
"""

lst = input('Введите 2 слова: ').split()

while len(lst) != 2 or lst[0].isdigit() or lst[1].isdigit():
    lst = input('Введите 2 слова: ').split()

# через срез
print('После перемены слов местами:', *lst[::-1])

# через метод .reverse
lst.reverse()
print('После перемены слов местами:', *lst)


# без метода .split
text = input('Введите 2 слова: ')
    
for index, item in enumerate(text):
    if item == ' ':
        stop = index
        a = text[:stop]
                
for index, item in enumerate(text):
    if item == ' ':
        start = index + 1
        b = text[start:]

lst_reverse = [b, a]
result = ' '.join(lst_reverse)

print(f'После перемены слов местами: {result}')
