"""
Написать 2 функции и оформить решение в виде модуля.
Даны координаты трех точек(x1, y1, x2, y2, x3, y3) (только положительные)
x1, y2 = input().split()
Первая функция вычисляет площадь треугольника.
Вторая функция должна определить, является ли треугольник прямоугольным.
"""


def get_storony(xy1,xy2,xy3):
    ax = xy2[0]-xy1[0]
    ay = xy2[1]-xy1[1]
    bx = xy3[0]-xy2[0]
    by = xy3[1]-xy2[1]
    cx = xy3[0]-xy1[0]
    cy = xy3[1]-xy1[1]
    a = round((ax**2 + ay**2)**0.5,2)
    b = round((bx**2 + by**2)**0.5,2)
    c = round((cx**2 + cy**2)**0.5,2)
    return a,b,c

def proove(a,b,c):
    if abs(abs(a) - abs(b)) < c:
        return True
    else:
        return False

def get_square(a,b,c):
    p = 0.5*(a+b+c)
    return round((p*(p-a)*(p-b)*(p-c))**0.5,2)

def chk_right(a,b,c):
    s = get_square(a,b,c)
    if (proove(1/2*a*b,s,0.01) or
        proove(1/2*a*c,s,0.01) or
        proove(1/2*b*a,s,0.01) or
        proove(1/2*b*c,s,0.01) or
        proove(1/2*c*a,s,0.01) or
        proove(1/2*c*b,s,0.01)):
        return True
    else:
        return False

x1,y1 = map(int,input('Enter point 1:(x y) ').split())
x2,y2 = map(int,input('Enter point 2:(x y) ').split())
x3,y3 = map(int,input('Enter point 3:(x y) ').split())
a,b,c = get_storony([x1,y1],[x2,y2],[x3,y3])
s = get_square(a,b,c)
rg = chk_right(a,b,c)
print(f'Storony = {a}, {b}, {c}; Square = {s}, This is right: {rg}')

