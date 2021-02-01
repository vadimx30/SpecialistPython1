# Дана строка из двух слов. Поменяйте эти слова местами.
# Пример:
# In: Hello Python
# Out: Python Hello

a = [i for i in input('Введите строку из двух слов: ').split()]
print(f'Введеная слова: {a}')
a = a[::-1]
print(*a)
