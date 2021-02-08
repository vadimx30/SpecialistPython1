"""
Написать 2 функции и оформить решение в виде модуля.
Даны координаты трех точек(x1, y1, x2, y2, x3, y3) (только положительные)
x1, y2 = input().split()
Первая функция вычисляет площадь треугольника.
Вторая функция должна определить, является ли треугольник прямоугольным.
"""

import func3
a = tuple(map(int, input('Введите кординаты первой точки: ').split()))
a = func3.proverka1(a)
b = tuple(map(int, input('Введите кординаты второй точки: ').split()))
b = func3.proverka1(b)
c = tuple(map(int, input('Введите кординаты третьей точки: ').split()))
c = func3.proverka1(c)
while a == b or b == c or a == c:
    print('Координаты точек совпадают, введите заново')
    a = tuple(map(int, input('Введите кординаты первой точки: ').split()))
    a = func3.proverka1(a)
    b = tuple(map(int, input('Введите кординаты второй точки: ').split()))
    b = func3.proverka1(b)
    c = tuple(map(int, input('Введите кординаты третьей точки: ').split()))
    c = func3.proverka1(c)
storona1 = func3.dlina(a, b)
storona2 = func3.dlina(a, c)
storona3 = func3.dlina(b, c)
print('Площадь треугольника = ', func3.striangle(storona1, storona2, storona3))
print(func3.proverka2(storona1, storona2, storona3))

#func3
import math

def proverka1(a: tuple) -> tuple:
    """Проверка на верность ввода координат"""
    while len(a) != 2 or a[0] < 1 or a[1] < 1:
        print('Вводить требуется две положительные координаты x и y')
        a = tuple(map(int, input('Введите кординаты первой точки: ').split()))
    return a

def dlina(point1: tuple, point2: tuple) -> float:
    """Вычисление длин сторон по координатам"""
    dlina = (point2[0] - point1[0]) ** 2 + (point2[1] - point1[1]) ** 2
    dlina = round(math.sqrt(dlina), 2)
    return dlina
    
def striangle(d1: float, d2: float, d3: float) -> float:
    """Вычисляем площадь по формуле Герона"""
    p = (d1 + d2 + d3) / 2
    s1 = p * (p - d1) * (p - d2) * (p - d3)
    s = round(math.sqrt(s1), 2)
    return s

def proverka2(d1: float, d2: float, d3: float) -> str:
    """Проверяем треугольник на прямой угол"""
    a = [d1, d2, d3]
    a.sort()
    d1 = a[0]
    d2 = a[1]
    d3 = a[2]
    result = ''
    if round(d3 ** 2, 2) == round((d1 ** 2 + d2 ** 2), 2):
        result = 'Треугольник прямоугольный'
    else:
        result = 'Треугольник не прямоугольный'
    return result
