# #  set - Множествo
# print(set(), type({}))
# a = {'a', 'b', 'c', 'a', 'c', 'c', 'd'}
# print(a)
# STRING = 'soteuhasth'
# b = set(STRING)
# print(b)
A = set([1, 2, 3, 4])
B = set([1, 5])
# B.add(7) # Добавление элемента к множеству
# print(len(A), A, len(B), B)
# C = set([10, 11, 12, 13])
# print(2 in A)
# print(2 in B)

# ## Удаление элемента из множества
# B.remove(7)

# print(f'{B = }') # Синт.сахар, работает только с версии 3.8
# print(f'B = {B}')

## Если элемента нет, получим ошибку
#B.remove(12)

## Удалим элемент, если он есть,
## Если элемента, то ошибку не будет
# C.discard(15)
# print(f'C = {C}')

# ## Удаляем элементы из множества до тех пор, пока оно не пустое.
# ## и выводим на консоль удаленные элементы
# while C:
#     print(C.pop())
#     print(C)
# print(C)
# ##  Можно удалить множество целиком,
# ##  но нельзя удалить отдельный элемент через команду del
### del B

print(f'A = {A}', id(A))
print(f'B = {B}', id(B))
# ## A | B
# ## A.union(B)
# # Возвращает множество, являющееся объединением множеств A и B.
print("A | B = ", A | B)
print(f'A = {A}') # Множество А не поменялось

A |= B   #! Множество А изменилось
# A.update(B)
# Добавляет в множество A все элементы из множества B.
print(f'A = {A}', id(A))

# # A & B
# # A.intersection(B)
# # Возвращает множество, являющееся пересечением множеств A и B.
print("A & B = ", A & B)
# # 
# # A &= B
# # A.intersection_update(B)
# # Оставляет в множестве A только те элементы, которые есть в множестве B.
A &= B
print("A &= B ", A)
# # 
# # # A - B
### A.difference(B)
### Возвращает разность множеств A и B
###(элементы, входящие в A, но не входящие в B).
A = set([1, 2, 3, 4])
B = set([1, 5])
print("A - B = ", A - B)
# # 
# # A -= B
# # A.difference_update(B)
# # Удаляет из множества A все элементы, входящие в B.
# A = set([1, 2, 3, 4])
# B = set([1, 5])
# print(id(A))
# A.difference_update(B)
# print('A.difference_update(B)', A)
# print(id(A))

# # A ^ B
# # A.symmetric_difference(B)
# # Возвращает симметрическую разность множеств A и B (элементы, входящие в A или в B, но не в оба из них одновременно).
A = set([1, 2, 3, 4])
B = set([1, 5])
print('A ^ B', A ^ B)

# # A ^= B
# # A.symmetric_difference_update(B)
# # Записывает в A симметрическую разность множеств A и B.
# A = set([1, 2, 3, 4])
# B = set([1, 5])
# A.symmetric_difference_update(B)
# print('A ^= B', A)
print('*' * 40)
A.add(5)
A.add(1)
print(A)
print(B)
# # A <= B
# # A.issubset(B)
# # Возвращает true, если A является подмножеством B.
print(B <= A)

# # A >= B
# # A.issuperset(B)
# # Возвращает true, если B является подмножеством A.
print(A >= B)
# # A < B
# # Эквивалентно A <= B and A != B
# print(A > B)
# # A > B
# # Эквивалентно A >= B and A != B
# print(A < B)
# 
# A.remove(5)
# A.discard(6)
# print(A)
# del_item = A.pop()
# print(f'del_item = {del_item}, A = {A}')

# сборки для множеств
s = {e for e in 'abcdonesosasa' if e not in 'ab'}
print(s)
temp = tuple(sorted(s))
print(temp)
print(set(temp)) # Set не гарантирует порядок, только уникальность
## В качестве элементов может быть кортеж
D = {1, (1, 2), (2, 3)}
print(D)