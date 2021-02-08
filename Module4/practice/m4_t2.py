'''
Даны  два  кортежа A и B, каждый  кортеж  состоит  из  N элементов.
Написать функцию для подсчета количества  тех  элементов  кортежа A,  для которых:
1) Ai > Bi
2) Ai = Bi
3) Ai < Bi
'''

import sys
from random import randint

def tuple_comparison_1 (tuple_a: tuple, tuple_b: tuple) -> tuple:
    '''сопоставление элементов кортежа a
    с соответствующими элементами кортежа b (a(i) vs b(i)):
   '''
    count_more = 0
    count_equal = 0
    count_less = 0
    for i in range(len(tuple_a)):
        if tuple_a[i] > tuple_b[i]:
            count_more += 1
        elif tuple_a[i] == tuple_b[i]:
            count_equal += 1
        else:
            count_less += 1
    return count_more, count_equal, count_less

def tuple_comparison_2 (tuple_a: tuple, tuple_b: tuple) -> tuple:
    '''сопоставление элементов кортежа a
    с каждым элементом кортежа b (a(i) vs b(i)...b(n)'''
    count_more = 0
    count_equal = 0
    count_less = 0
    for i in range(len(tuple_a)):
        x = 0
        while x < len(tuple_b): 
            if tuple_a[i] > tuple_b[x]:
                count_more += 1
            elif tuple_a[i] == tuple_b[x]:
                count_equal += 1
            else:
                count_less += 1
            x +=1
    return count_more, count_equal, count_less

def main():
    z = int(input('Введите количество элементов (N): '))
    tuple_a = tuple(randint(1, 100) for _ in range(z))
    tuple_b = tuple(randint(1, 100) for _ in range(z))
    param = input('Выберите вид сопоставления:\n'
                  '1: попарное сопоставление ((a(i) vs b(i)),'
                  ' результат = N, или\n'
                  '2: сопоставление с каждым элементом b (a(i) vs b(i)...b(n),'
                  ' результат = N^2\n')
    
    if param == '1':
        count_more = (tuple_comparison_1 (tuple_a, tuple_b))[0]
        count_equal = (tuple_comparison_1 (tuple_a, tuple_b))[1]
        count_less = (tuple_comparison_1 (tuple_a, tuple_b))[2]
    elif param == '2':
        count_more = (tuple_comparison_2 (tuple_a, tuple_b))[0]
        count_equal = (tuple_comparison_2 (tuple_a, tuple_b))[1]
        count_less = (tuple_comparison_2 (tuple_a, tuple_b))[2]
    else:
        print('Необходимо выбрать тип сравнения')
        sys.exit()
         
    print(f'{count_more = }\n'
          f'{count_equal = }\n'
          f'{count_less = }')

if __name__ == '__main__':
    main()
