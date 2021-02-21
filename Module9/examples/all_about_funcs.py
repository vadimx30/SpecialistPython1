# Функция полноправный объект в языке Python:
# • может быть создан во время выполнения;
# • может быть присвоен переменной или полю структуры данных;
# • может быть передан функции в качестве аргумента;
# • может быть возвращен функцией в качестве результата.

def func(text:str) -> str:
    return text.upper() + '!'
# 
# 
# print(func('привет'))
# 
bar = func
# print(type(bar), bar) 
# print(bar('пока'))
# 
# # Можно удалить func, но bar будет вызываться
# del func
# # # print(func('textest')) ## Out -> Error
# # # 
# print(bar('Я работаю'))
# print(bar.__name__)

# 
# ## Можно хранить функции в структурах данных
# funcs = [bar, str.lower, str.capitalize]
# print(funcs)
# # # 
# # # ## Доступ в функциям, хранящимся внутри списка
# for function in funcs:
#      print(function.__name__, '->', function('проверка Работы'))
# 
# ## Вызов функции как элемента списка по индексу 
# print(funcs[0]('первая функция'))


# ## Передача функции в другую функцию
def greet(func):
    greeting = func('Программа на Python')
    print(greeting)

## Вызов функции greet с аргументом - функцией bar 
# greet(bar)
# # # 
# def imp_func(text):
#      return text.lower() + '. Done!'
# 
# ## Вызов функции greet с аргументом - функцией imp_func
# greet(imp_func)

# ## Функции более высокого порядка(higher-order functions)
# ## map, filter, reduce
# print(map(bar, ['hello', 'hi', 'привет']))
# print(set(map(bar, ['hello', 'hi', 'привет'])))
# # # 
# def condition(text):
#      return True if len(text) > 3 else False
# # ## Включаем элемент в итоговый список, если результат работы
# # ## функции condition True
# print(list(filter(condition, ['hello', 'hi', 'привет'])))
# # #
# def add_two(a, b):
#      return a + b
# # 
# from functools import reduce
# print(reduce(add_two, ['hello', 'hi', 'привет']))
# 
# ## Пример функции zip
# a = list(range(5))
# b = list(range(11, 16))
# print(list(zip(a, b)))
# 
# ## Вложенные функции
# def main(text:str):
#     a = 5
#     def inner_func(text_1:str):
#         nonlocal a
#         a += 1
#         return text_1.lower() + '...' + f'{a}'
#     print(locals()) ## Словарь локальных переменных
# 
#     return inner_func(text)
# 
# print(main('Привет, Всем '))
# 
# print(inner_func('Может работает?')) # Error
# print(main.inner_func) # Error

## Результат работы функции main это идентификатор на функцию,
## которая выбирается в зависимости от значения аргумента
# def main_imp(size: int):
#     def foo(text):
#         return text.lower() + '...'
#     def bar(text):
#         return text.upper() + '!!!'
#     if size > 5:
#         return foo
#     else:
#         return bar
# # # 
# print(main_imp(3)) ## out-> function main_imp.<locals>.bar
# print(main_imp(7)) ## out-> function main_imp.<locals>.foo
# some_name = main_imp(1)
# print(some_name, type(some_name))
# print(some_name('привет'))
# # 
# ## Замыкания
# def main_better(text:str, size:int):
#     def foo():
#         print("You have called foo() function, "
#               f"because {size} > 5")
#         print(locals())
#         return text.lower() + '...'
#     def bar():
#         print("You have called bar() function, "
#               f"because {size} < 5")
#         print(locals())
#         return text.upper() + '!!!'
#     if size > 5:
#         return foo
#     else:
#         return bar
# # 
# print(main_better('Как Дела?', 7)())  ## out -> foo
# print('*' * 40)
# print(main_better('Как Дела?', 3)())  ## out -> bar
# print('*' * 40)
# print(main_better('хорошо', 7)())
# print('*' * 40)
# print(main_better('хорошо', 3)())
# 
# ## Создание фабрики функций 
# def make_adder(n):
#     def add(x):
#         print(locals())
#         return x + n
#     return add
# # 
# ## Создали функцию, которая будет возвращать сумму любого числа с тройкой
# plus_3 = make_adder(3)
# ## Создали функцию, которая будет возвращать сумму любого числа с пятеркой
# plus_5 = make_adder(5)
# print(plus_3)
# print(plus_3(7))   ## out -> 10
# print(plus_5(10))  ## out -> 15
# print(make_adder(100)(99))
# 
# ## Лямбды. Нельзя делать связывание в теле функции
# add = lambda x, y: x + y
# print(add(2, 3), type(add))
# 
# # # Вызов лямбды с аргументами
# print((lambda x, y: x + y)(10, 16))

# # Сортировка по второму значению кортежей
# list_of_tuples = [(1, 'd'), (2, 'b'), (4, 'a'), (3, 'c')]
# print(sorted(list_of_tuples, key=lambda x: x[1]))
# # # 
# print(sorted(range(-5, 6), key=lambda x: x * x))
# # 
# # ## Та же самая функция, что и make_adder, только с использованием lambda
# def make_adder_lambda(n):
#     return lambda x: x + n
# # # 
# plus_3 = make_adder_lambda(3)
# plus_5 = make_adder_lambda(5)
# print(plus_3(4))
# print(plus_5(4))
# 
# ## Декораторы
# def null_decorator(func):
#     return func
# # 
# def greet():
#     return 'Привет!'
# 
# ## Механизм работы декоратора
# greet = null_decorator(greet)
# # 
# print(greet())

## Функция декоратор
# def uppercase(func):
#     def wrapper():
#         original_result = func()
#         #print(original_result)
#         modified_result = original_result.upper()
#         return modified_result
#     return wrapper
# 
# ## Декоратор
# @uppercase  ## тоже самое, что и greet_eng = uppercase(greet_eng)
# def greet_eng() -> str:
#     return 'Hello!'
# 
# print(greet_eng()) ## out -> HELLO
# # 
# print(greet)
# print(null_decorator(greet))
# print(uppercase(greet_eng))
# # 
# # ## Применение нескольких декораторов
# def strong(func):
#     def wrapper():
#         return '<strong>' + func() + '</strong>'
#     return wrapper
# 
# def emphasis(func):
#     def wrapper():
#         return '<em>' + func() + '</em>'
#     return wrapper
# # # 
# # ## Порядок применения снизу вверх
# @strong
# @emphasis
# def greet2():
#     return 'Привет!'
# # 
# print(greet2())

## Функция декоратор
def trace(func):
    def wrapper(*args, **kwargs):
        print(f'ТРАССИРОВКА: вызвана {func.__name__}() '
            f'с {args}, {kwargs}')
        original_result = func(*args, **kwargs)
        print(f'ТРАССИРОВКА: {func.__name__}() '
        f'вернула {original_result!r}')
        return original_result + '!!!!'
    return wrapper

@trace
def say(name, line):
    return f'{name * 3}: {line}'

print(say('hi', line='Hello'))
print(say(100, 5.2))

