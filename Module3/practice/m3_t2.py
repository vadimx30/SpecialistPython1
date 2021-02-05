"""
Определите, сколько букв содержит самое длинное слово в строке.
Пример:
In: Как дела в учебе
Out: 5
"""
text = input('Enter:').split()
text.sort(key = len)
a = len(text[-1])
print(a)
