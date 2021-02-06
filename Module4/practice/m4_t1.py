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

def param(a: float, b: float) -> tuple:
    '''определение площади'''
    perimetr = a * 2 + b * 2
    s = a * b
    return perimetr, s

def zabor(perimetr: float, zabor_price: float) -> float:
    '''определение стоимости забора'''
    zabor_cost = perimetr * zabor_price
    return zabor_cost

def acrage(s: float, acrage_price: float) -> float:
    '''определение стоимости земельного участка'''
    acrage_cost = s * acrage_price
    return acrage_cost

def main():
    a = float(input('Длина: '))
    b = float(input('Ширина: '))
    zabor_price = float(input('Цена погонного метра забора: '))
    acrage_price = float(input('Цена квадратного метра земли: '))
    
    perimetr, s = param(a, b)
    zabor_cost = zabor(perimetr, zabor_price)
    acrage_cost = acrage(s, acrage_price)
    print('Параметры (периметр и площадь):', *(param(a, b)))
    print('Стоимость забора:', zabor_cost)
    print('Стоимость участка:', acrage_cost)

if __name__ == '__main__':
    main()
