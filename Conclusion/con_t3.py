""" 3. Написать функцию, используя набор букв из модуля string(string.ascii_lowercase),
    которая расшифрует строку. Каждая буква - это две цифры.
    Отчет с 00 -> 'a' и до 25 -> 'z', 26 - это пробел, он не входит в набор букв
    Вход: строка из цифр. Выход: Текст.
    Проверка работы функции выполняется через вторую строку.
"""

import string, re
code = '070411111426152419071413'
list_letters = list(string.ascii_lowercase)
list_letters.append(' ')
list_numbers = ('00', '01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26')
list_code = re.findall(r'\d\d', code)
zipped = list(zip(list_numbers, list_letters))
print(zipped)
# print(zipped[0][0])
# for i in zipped:
#     for j in zipped[i]:
#         if j == zipped[i][j]:
#             print(zipped[i][j])
