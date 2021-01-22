name = input('Как вас зовут?>')
print('Здравствуйте,', name)
age = int(input('Сколько Вам лет?>'))
print('Вам', age, 'лет.')


# Параметры sep(по умолчанию ' ') и end (по умолчанию '\n')
# print(name, age, sep='|')
# print("Здравствуйте,", name, ".", end=' ')
# print("Вам", age, "лет.")
# 
# ### 1-й способ - это %
# print('Result of our program %s and %s. Two values.' % (name, age))
# print('Result of our program %s. First value.' % name) # одна переменная
# # 
# print('Result of our program %s and %d. Two values.' % (name, age))
# ## Вывод переменной с типом float
# ## с ограничением в 2 разряда после запятой
# print('Result of our program %.2f. First value.' % (age / 3))
# 
# ### 2-й способ - функция format
# print('Your name is {}. You are {}.'.format(name, age))
# print('You are {1}. Your name is {0}.'.format(name, age))
# print('You are {1}. Your name is {0}.'.format(name, age / 3))
# print('You are {1:.2f}. Your name is {0}.'.format(name, age / 3))
# print('You are {1:10.2f}. Your name is {0}.'.format(name, age / 3))
# 
### 3-й способ - f-string
print(f'Your name(three times) is {name}. You are {age}.')
# Можно подставлять и выражения
print(f'Your name(three times) is {name * 3}. You are {age / 2}.')
# 
# 
# import math
# # 
# print('Hello {}'.format('World')) 
# print('{}'.format(math.pi))
# print('{0:.2f}'.format(math.pi)) 
# print('{0:+.2f}'.format(5))
# print('{:.2e}'.format(3000))
# print('{:0>6d}'.format(5)) # Шесть позиций под вывод и заполнение нулями слева
# print('{:x<7d}'.format(5))
# print('{:,}'.format(1000000))
# print('{:.1%}'.format(0.25)) # умножить на 100 и добавить знак %
# print('{0}{1}'.format('a', 'b'))
# print('{1}{0}'.format('a', 'b'))
# print('{num:}'.format(num=7))




