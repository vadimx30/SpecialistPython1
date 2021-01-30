### Tuples - кортежи - неизменяемый список
# b = tuple()
# d = 1, 2, 5, 5, 4 
# print(d)
# a = tuple(range(11))
# print(a)
# ### a[1] = 99 # Это ошибка
# print(a.count(9))
# print(d.index(5))
# 
## Генератор выражений (Пример ленивых вычислений)
b = (i ** 3 for i in range(11))

import sys
for i in b:
    print(i, end=' ')
# 
print('\n' + '*' * 30)
print('size of b:', sys.getsizeof(b))
print(list(b))
# 
# #     
c = ([1, 2], [3, 4], [5, 6])
print(c, type(c))
c[0][1] = 99 # Есть такая возможность
print(c)
d = (3, 5, 8, 1, 9)
d = tuple(sorted(d))
print(d)
# 
## Считываем две координаты и приводим их к int
## Примеры
point_one = tuple(map(int, input('Enter x and y: ').split()))
print(point_one)
x, y = map(int, input('Enter x and y: ').split())
print(x, y)
 
