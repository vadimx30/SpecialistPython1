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

def main(): 
    box_1 = sorted(tuple(map(int, input('Размер коробки № 1: ').split())))
    while (len(box_1) != 3 or
           any(box_1[i] < 1 for i in range(len(box_1)))):
        box_1 = sorted(tuple(map(int, input('Размер коробки № 1: ').split())))
        
    box_2 = sorted(tuple(map(int, input('Размер коробки № 2: ').split())))
    while (len(box_2) != 3 or
           any(box_2[i] < 1 for i in range(len(box_2)))):
        box_2 = sorted(tuple(map(int, input('Размер коробки № 2: ').split())))
    
    if all(box_1[i] > box_2[i] for i in range(len(box_1))):
            print('Коробка 2 входит в Коробку 1')
    elif all(box_1[i] < box_2[i] for i in range(len(box_1))):
            print('Коробка 1 входит в Коробку 2')
    else:
        print('Коробки не совместимы')
    
if __name__ == '__main__':
    main()  
