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

import func
a = float(input('Введите длину участка: '))
b = float(input('Введите ширину участка: '))
spm = float(input('Введите стоимость погонного метра забора: '))
skm = float(input('Введите стоимость квадратного метра земли: '))
p, s = func.param(a, b)
print('Стоимость забора: ', func.summzabor(p, spm))
print('Стоимость земли: ', func.summearth(s, skm))

# Модуль с функциями
def param(a: float, b: float) -> tuple:
    perimetr = (a + b) * 2
    perimetr = round(perimetr, 2)
    ploshad = a * b
    ploshad = round(ploshad, 2)
    return perimetr, ploshad

def summzabor(p: float, spm: float) -> float:
    zabor = p * spm
    zabor = round(zabor, 2)
    return zabor

def summearth(s: float, skm: float) -> float:
    earth = s * skm
    earth = round(earth, 2)
    return earth
