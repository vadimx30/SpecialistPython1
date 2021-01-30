# for _ in range(10):
#     print('Python')

## изменяемый тип данных - Списки

# a = [1, 2, 'hello', 8.3, True]
# print(type(a))
# print(a)
# b = []      # Пустой список
# c = list()  # Пустой список
# print(type(b), type(c))
# 
# lst = list(range(11))
# print('lst: ', lst)
# # # 
# for item in a:
#     print(item)
# #
# print('id of a: ', id(a))
# print('Доступ по индексу')
# for index in range(len(a)):
#     a[index] = index
#     
# # Резделение двух выражений с помощью ';'
# print(a); print('Длина списка: ', len(a))
# print('id of a: ', id(a))


# a.append(5) # добавление элемента
# print('list a:', a)
# result = []
# s = 'satuhsatuhsanthusn'
# count = 0
# vowels =['a', 'o', 'e', 'u', 'i']
# for char in s:
#     if char in vowels:
#         count += 1
#     else:
#         result.append(char)
# print(count)
# print(result)
# s1 = ''.join(result) # Собираем из списка строку
# print('s1: ', s1)

## Делаем копию списка с другим id
# b = a.copy()
# print('b', b)
# a[0] = 99
# print(a)
# print(b)
# 
# ## Выводит количество вхождений элемента в список
# print(b.count(1))
# 
# ## Увеличивает список за счет другого списка
# a.extend([10, 11])
# print('list a: ', a)
# # 
# # # ## Индекс элемента в списке
# print('index of 10 is {1} and index of 1 is {0}'.format(a.index(1), a.index(10)))
# 
# # # ## Удаление элемента списка
# a.pop()
# del_item = a.pop(3) # можем удалить элемент с указанным индексом
# print('del_item - {}'.format(del_item))
# print(a)
# 
# a.remove(10) # удаляем элемент по значению, ошибка если элемента не в списке
# print(a)
# 
# ##Разворачиваем и сортируем список 
# a.reverse()
# print(a)
# # a.sort()
# # print(a)
# ## Вставка элемента на определенный индекс
# a.insert(2, '4')
# print(a)


# c = a.copy()
# print('list c: ', c)
# ## Очищаем список от значений. Результат - пустой список
# c.clear()
# print('list c: ', c)
# c.append(2)
# 
# # 
# # 
# print(a)
# print(*a) # * это операция распаковки
# 
# first_element = a[0]
# last_element = a[-1]
# print(first_element, last_element)
# 
# # # Используем звездочки для нужного связывания
# _, s, *_, l = a
# print(s, l)
# # 
# # 
# # # Тернарный оператор (однострочник)
# ## Если условие True возвращаем c, иначе d
# c = 'Есть'
# d = 'Нет'
# result = c if 1 in a else d  #
# print(result)


# str1 = 'Это пустой список'
# str2 = 'Это не пустой список'
# res = str2 if c else str1
# print('list c - ', res)
# 
# ## Удаление элемента с помощью del
# print(a)
# del a[-2]
# print(a)
## Удаление объекта целиком
# del a
# print(a)

# lst = list(range(10)) 
# ## Срезы - Slices
# ## list[start:stop:step]
# 
# print(lst)
# print(lst[2:7])
# print('lst[2:8:2] ->', lst[2:8:2])
# print(lst[:3]) # Первые три элементов
# print(lst[-5:]) # Последние пять элементов
# # 
# new_lst = lst[:] # Копируем список
# print(new_lst)
# print('Reversed lst:', lst[::-1])
# # 
# #
# s = 'hello, students!'
# for index, item in enumerate(s):
#     # print(f'{index}: {item}')
#     if item == ',':
#         stop = index
# print(s[:stop])

#     
## Генератор списков
lst = [i ** 2 for i in range(11)]
print(lst)
temp_lst = [1, "2", 3, 4, 5, 6, "hello", 8, 9, 0, '11', True, 5.1]
result = [(type(i) != str) for i in temp_lst]
print(result) # out -> [True, False, True, True, True, True, False, True, True, True, False, True, True]
result_1 = [item for item in temp_lst if type(item) != str]
print(result_1) #out -> [1, 3, 4, 5, 6, 8, 9, 0, True, 5.1]


# # # # all() -> True, eсли все значения True
# # # # any() -> True, если хотя бы одно значение True
# print(result)
# print(all(result))
#
## Результат - список квадратов нечетных чисел от 0 до 10
lst_1 = [i ** 2 for i in range(11) if i % 2]
print(lst_1)

## Создаем большой список из других списков
big_list = [lst, lst_1, result, temp_lst]
print(big_list)


