# Задача №4
"""
Вход:
    расстояние(50 - 10000 км),
    расход в литрах (5-25 литров) на 100 км и
    стоимость бензина(константа) = 48 руб

Выход: стоимость поездки в рублях
"""

a = int(input('Расстояние (50 - 10000 км):'))
b = int(input('Расход (5 - 25 л на 100 км):'))
c = 48
if 10000 > a < 50 or 25 > b < 5:
    print('Error')
else:
    print(a * (b / 100) * c)
