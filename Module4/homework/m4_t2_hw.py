"""
Написать 2 функции и оформить решение в виде модуля.
Даны координаты трех точек(x1, y1, x2, y2, x3, y3) (только положительные)
x1, y2 = input().split()
Первая функция вычисляет площадь треугольника.
Вторая функция должна определить, является ли треугольник прямоугольным.
"""

import math
import sys

def check(side_ab: float, side_bc: float, side_ca: float):
    '''проверка на существование треугольника'''
    if (side_ab + side_bc > side_ca and
        side_ab + side_ca > side_bc and
        side_bc + side_ca > side_ab):
        return
    else:
        print("Треугольник не существует")
        sys.exit()


def triangle_square(side_ab: float, side_bc: float, side_ca: float) -> float:
    '''вычисление площади треугольника'''
    #√(p(p-a)(p-b)(p-c))
    half_perimetr = (side_ab + side_bc + side_ca) / 2
    s = math.sqrt(half_perimetr
                  * (half_perimetr - side_ab)
                  * (half_perimetr - side_bc)
                  * (half_perimetr - side_ca))
    return round(s, 2)


def right_triangle_check(side_ab: float, side_bc: float, side_ca: float) -> str:
    '''проверка: является ли треугольник прямоугольным'''
    if (round(side_ab**2, 2) == round((side_bc**2 + side_ca**2), 2) or
        round(side_bc**2, 2) == round((side_ab**2 + side_ca**2), 2) or
        round(side_ca**2, 2) == round((side_ab**2 + side_bc**2), 2)):
        return print ('Треугольник является прямоугольным')
    else: 
        return print ('Треугольник не является прямоугольным')


def main():
    vertex_a = tuple(map(int, input('Координаты вершины А: ').split()))
    while (len(vertex_a) > 2 or
           len(vertex_a) < 2 or
           vertex_a[0] < 0 or vertex_a[1] < 0):
        vertex_a = tuple(map(int, input('Координаты вершины A: ').split()))

    vertex_b = tuple(map(int, input('Координаты вершины B: ').split()))
    while (len(vertex_b) > 2 or
           len(vertex_b) < 2 or
           vertex_b[0] < 0 or vertex_b[1] < 0):
        vertex_b = tuple(map(int, input('Координаты вершины B: ').split()))

    vertex_c = tuple(map(int, input('Координаты вершины C: ').split()))
    while (len(vertex_c) > 2 or
           len(vertex_c) < 2 or
           vertex_c[0] < 0 or vertex_c[1] < 0):
        vertex_c = tuple(map(int, input('Координаты вершины C: ').split()))

    #√((X2-X1)²+(Y2-Y1)²)
    # для точности дальнейших расчетов - не округлять
    side_ab = math.sqrt((vertex_b[0] - vertex_a[0])**2
                        + (vertex_b[1] - vertex_a[1])**2)
    side_bc = math.sqrt((vertex_c[0] - vertex_b[0])**2
                        + (vertex_c[1] - vertex_b[1])**2)
    side_ca = math.sqrt((vertex_a[0] - vertex_c[0])**2
                        + (vertex_a[1] - vertex_c[1])**2)
    
    check(side_ab, side_bc, side_ca)
    
    result = triangle_square(side_ab, side_bc, side_ca)
    print(f'Площадь треугольника = {result} кв.ед.')
    right_triangle_check(side_ab, side_bc, side_ca)

if __name__ == '__main__':
    main()
