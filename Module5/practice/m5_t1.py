'''
Задача №1 Объемы.
Вход: объемы двух коробок:
a, b, c - длина, ширина и высота первой коробки
k, n, m - длина, ширина и высота первой коробки
толщину коробку не учитывать! 
Коробки можно переворачивать.
Выход: входит ли одна коробка в другую или нет
Ответы: Первая входит во вторую, вторая входит в первую или они не совместимы.
'''

import func4
a = tuple(map(int, input('Введите размеры первой коробки: ').split()))
a = func4.proverka1(a)
b = tuple(map(int, input('Введите размеры второй коробки: ').split()))
b = func4.proverka1(b)
print(func4.proverka2(a, b))

# func4
def proverka1(a: tuple) -> tuple:
    """Проверка на верность ввода раметров коробки"""
    while len(a) != 3 or a[0] < 0 or a[1] < 0 or a[2] < 0:
        print('У коробки должно быть 3 параметра и все больше 0')
        a = tuple(map(int, input('Введите правильные параметры: ').split()))
    return a

def proverka2(a: tuple, b:tuple) -> str:
    a = tuple(sorted(a))
    b = tuple(sorted(b))
    result = ''
    i = 1
    if a[0] > b[0]:
        while i < 3:
            if a[i] > b[i]:
                result = 'Вторая коробка входит в первую'
            else:
                result = 'Коробки нельзя вложить одну в другую'
                break
            i += 1
    elif a[0] < b[0]:
        while i < 3:
            if a[i] < b[i]:
                result = 'Первая коробка входит во вторую'
            else:
                result = 'Коробки нельзя вложить одну в другую'
                break
            i += 1
    return result
