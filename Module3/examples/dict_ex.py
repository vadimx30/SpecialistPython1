from pprint import pprint

## Dictionaries - Словари(структуры данных для пар "ключ-значение")
## {key: value}
# dict_n = {1: [3, 1, 4], 2: 4.1, 3:'value', (4, 5): True, 'first': 6}
# # print(dict_n)
# dict_n[3] = 'changed_value'
# dict_n['first'] = 99
# # print(dict_n)
# ## print(dict_n['second']) ## KeyError нет такого ключа
# dict_n['second'] = 12
# # print(dict_n)

# dict_a = dict(name = (2, 5), surname = '2')
# print(dict_a)
# # 
# ##Генератор словарей
# dict_m = {str(i): i * 2 for i in range(10)}
# pprint(dict_m) ## Красивый вывод словаря
# print(len(dict_m))

## Функция hash может быть применима только к unmutable объектам
# print(hash((2, 5)))
# print(hash('name'))
# print(hash('surname'))
# print(hash(2))
# print(hash(9.5))
# # 
# dict_n[4] = 'new value'
# print(dict_n)
# print('Builtins methods for dictionaries')
# print(dict_n.keys())  # Список только ключей
# print(dict_n.values()) # Список только значений
# print(dict_n.items()) #Список пар
# 
# for key, value in dict_n.items():
#     print(f'{key}: {value}')
# 
# print('first' in dict_n)
# print('third' not in dict_n)
# print('*' * 40)
# print(dict_n)
# for key in dict_n:
# # for key in dict_n.keys(): # то же самое
#     print(dict_n[key] * 2)
# # 
# print('Before: ', dict_n)
# del_item = dict_n.pop(2)
# print('After: ', dict_n)
# # #del_item = dict_n.pop() ## Error
# print('{} value of key 2'.format(del_item))
# # # print('len = ', len(dict_n))
# del_k_v_item = dict_n.popitem()
# print(dict_n)
# print(del_k_v_item)
# # 
# if 13 not in dict_n.values():
#     dict_n['add'] = 13
# print(dict_n)
# 
#words = {}  ##Пустой словарь - Falsy value
# words = {'string': 'value'}
# words.update({'more_values': 999, 'a': 7})
# print(words)
# print(words.get('c')) # Вернет None, ошибки не будет
# print(words.setdefault('b', 'значение по умолчанию'))
# print(words)
# # 
# # ## Удаление пары(ключ-значение) по ключу
# del words['b']
# print(words)
# # 
# students =  {1122: ('Name', 'Surname', 'age', 'address'),
#              1133: ('a_name', 'a_Surname','a_age', 'a_address')}
# for key in students:
#     if key == 1122:
#         print(students[key][3])
# # #         
# people =  {'Petrov': {'prof': 'student', 'age': 23},
#             'Ivanov': {'prof': 'teacher','age': 43}}
# print('Вложенные словари: ')
# for key in people:
#     print(people[key]['prof'])
# 
# # 
