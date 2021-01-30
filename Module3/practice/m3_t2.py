"""
Определите, сколько букв содержит самое длинное слово в строке.
Пример:
In: Как дела в учебе
Out: 5
"""


string = [i for i in input('Enter string: ').split()]
s = 0
for i in string:
    if s < len(i):
        s = len(i)
print(f'Maximum chars is {s}')
