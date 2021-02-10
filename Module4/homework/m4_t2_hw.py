"""
Написать 2 функции и оформить решение в виде модуля.
Даны координаты трех точек(x1, y1, x2, y2, x3, y3) (только положительные)
x1, y2 = input().split()
Первая функция вычисляет площадь треугольника.
Вторая функция должна определить, является ли треугольник прямоугольным.
"""

import sys, math

def func_1(a: tuple, b: tuple, c: tuple):
    s_abc = 0.5 * math.fabs((b[0] - a[0]) * (c[1] - a[1]) - (c[0] - a[0]) * (b[1] - a[1]))
    print(f'Площадь треугольника = {s_abc}')
    
def func_2(a: tuple, b: tuple, c: tuple):
    ab = math.sqrt((b[0] - a[0]) ** 2 + (b[1] - a[1]) ** 2)
    bc = math.sqrt((c[0] - b[0]) ** 2 + (c[1] - b[1]) ** 2)
    ca = math.sqrt((a[0] - c[0]) ** 2 + (a[1] - c[1]) ** 2)
    
    if (ab ** 2 == bc ** 2 + ca ** 2) or (bc ** 2 == ab ** 2 + ca ** 2) or (ca ** 2 == ab ** 2 + bc ** 2):
        print('Прямоугольный треугольник')
    else:
        print('НЕ прямоугольный треугольник')
    
def main():
    a = tuple(map(int, input('Первая точка: ').split()))
    b = tuple(map(int, input('Вторая точка: ').split()))
    c = tuple(map(int, input('Третья точка: ').split()))
    func_1(a, b, c)
    func_2(a, b, c)

if __name__ == '__main__':
    main()
