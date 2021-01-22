
# print(type(True), type(False))
# 
# data = int(input('Enter value: '))

## Шаблон
## if условие верно(True): 
##     Блок инструкций 1
## elif условие верно:
##     Блок инструкций 2
## elif условие верно:
##     Блок инструкций 3
## elif условие верно:
##     Блок инструкций 4
## elif условие верно:
##     Блок инструкций 5
## else:
##     Блок инструкций 6

# 
# if data > 0:
#     print('Число положительное')
# elif data < 0:
#     print('Число отрицательное')
# else:
#     print('Число равно 0')

# == равно
# != не равно
# <  меньше
# <= меньше или равно
# >  больше 
# >= больше или равно
# in входит в объект
# not in не входит в объект
# st = 'Hello'
# print('e' in st)
# print('a' in st)
#     
# data = '' # Пустая строка  Falsy value
# 
# if data: # Если data равно 0 или пустой строке, то значение выражения - False
#          # Если data не равно 0 или пустой строке, то значение выражения - True
#     print('Data is not null')
# else:
#     print('Data is null')
# #

# 
n = int(input('Enter a number(1-1000): '))
m = int(input('Enter a number(1-1000): '))
# 
# 
# ### Логические операторы and, or, not
##Логическое 'И'
if n > 0 and m < 100: # True and True
    print('Первая проверка пройдена')
##Логическое 'ИЛИ'. Ленивый оператор
if n > 0 or m < 100:  # True or False -> True; False or True -> True
    print('Вторая проверка пройдена')
#     
#
n /= 1 ## n = n / 1 -> результат будет типа float
if type(n) == int:
    print('Целое число')
else:
    print('Дробное число')
    

n += 1 ## n = n + 1 -> результат будет типа int
if type(n) == int:
    print('Целое число')
else:
    print('Дробное число')
    
    