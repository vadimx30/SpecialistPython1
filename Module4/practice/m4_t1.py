"""
Написать 3 функции и оформить решение в виде модуля.
Дан участок земли прямоугольной формы.
Нужно посчитать стоимость самой земли и забора по периметру.

Первая функция принимает в качестве аргументов длину и ширину участка.
Возвращает периметр и площадь.

Вторая функция принимает в качестве аргументов периметр и стоимость погонного метра забора.
Возвращает итоговую сумму.

Третья функция принимает в качестве аргументов площадь и стоимость одного квадратного метра земли.
Возвращает итоговую сумму.
"""
## Fails №1
# import completing_4
# a = float(input('Dlina: '))
# b = float(input('Shirina: '))
# c = float(input('$ metra: '))
# d = float(input('$ metra*2: '))
# p, s = completing_4.param(a, b)
# print('$ zabora: ', completing_4.summzabor(p, c))
# print('$ zemli: ', completing_4.summearth(s, d))
# 
## Fails №2
# def param(a: float, b: float) -> tuple:
#     perimetr = (a + b) * 2
#     perimetr = round(perimetr, 2)
#     ploshad = a * b
#     ploshad = round(ploshad, 2)
#     return perimetr, ploshad
# def summzabor(p: float, spm: float) -> float:
#     zabor = p * spm
#     zabor = round(zabor, 2)
#     return zabor
# def summearth(s: float, skm: float) -> float:
#     earth = s * skm
#     earth = round(earth, 2)
#     return earth
