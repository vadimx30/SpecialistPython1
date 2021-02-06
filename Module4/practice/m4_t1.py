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
#mymodule.py
def getPS(a:float,b:float):
    p = a+a+b+b
    s= a*b
    return p,s

def getSumZabor(p:float,c:float):
    return p*c

def getSumEarth(s:float,c:float):
    return s*c
#end mymodule.py

import mymodule
a = float(input('Enter a: '))
b = float(input('Enter b: '))
c = float(input('Enter c of zabor: '))
cc = float(input('Enter c of earth: '))

p,s = mymodule.getPS(a,b)
cz = mymodule.getSumZabor(p,c)
ce = mymodule.getSumEarth(s,cc)

print(f'perim = {p}, square = {s}, Zabor = {cz}, Earth = {cz}')
