from functools import reduce
import operator
from operator import mul, add, itemgetter


# def fact(n: int) -> int :
#     return reduce(lambda a, b: a * b, range(1, n + 1))
# 
# print(fact(5))
# # print(fact(0)) # <- Error
# 
# def fact_r(n:int):
#         return 1 if n == 0 else n * fact_r(n - 1)
# 
# print(fact_r(5))
# 
# def fact_o(n):  
#     return reduce(mul, range(1, n + 1))
# 
# print(fact_o(5))
# 
# ### Возращает все методы и атрибуты модуля operator
# # print([name for name in dir(operator) if not name.startswith('_')])
# 
# number_tuples = [('first', 'A', 15), 
#                 ('second', 'B', 12), 
#                 ('third', 'B', 10)
#                 ]
# print(sorted(number_tuples, key=lambda number: number[2]))
# 
# print(sorted(number_tuples, key=itemgetter(2)))
# 
# print(sorted(number_tuples, key=itemgetter(1, 2)))
# print(sorted(number_tuples, key=itemgetter(1, 2), reverse=True))
# 
# print(sorted(number_tuples, key=lambda number: len(number[0])))
# 
# lst = [[40, 2, 4, 12], [4, 8, 9, 1, 9, 11], [23, 1, 23]]
# 
# new_lst = sorted(lst, key=len)
# print(id(lst), id(new_lst))
# print(new_lst)
# print(sorted(lst, key=sum))



dict_ex = {'one':4, 'temp': 2, 'second':2, 'third':6}
print(sorted(dict_ex))
print(sorted(dict_ex, key=len))

# ## Сортировка по значениям
print(sorted(dict_ex, key=lambda x: dict_ex.get(x)))
print(sorted(dict_ex, key=dict_ex.get))
# 
school_class = [{'name': 'Ivanov', 'value': 5}, 
                {'name': 'Petrov', 'value': 3},
                {'name': 'Sidorov', 'value': 4}]
                
print(max(school_class, key=lambda x: x['value']))
print(min(school_class, key=lambda x: x['value']))

texts = ['iiiii', 'bag', 'veto', 'blackboard', 'sequoia']
# 
# ### Пример перегруженной строки
# ### Слишком сложно и нужно разбивать на читабельный текст
print(sorted(texts, key=lambda x: len(set(
         [l for l in list(x) if l in ['a','e','i','o','u']]))))
# 
# def number_distinct_vowels(x):
#     vowels = ['a', 'e', 'i', 'o', 'u']
#     vowels_only = [l for l in list(x) if l in vowels]
#     distinct_vowels = set(vowels_only)
#     return len(distinct_vowels)
# 
# print(sorted(texts, key=number_distinct_vowels))