### Циклы

## Инициализация
## while Условие:
##     Тело цикло(инструкции)
##     Изменение условия

# 
# a, b = 2, 30
# while a < b:  ## 
# #     <block of intructions>
#     print('a =', a)
#     a += 2
#     if a == 12: ## Переходим на новый цикл, пропуская выполнение print
#         print('Перехожу на новую проверку')
#         continue
#     if a == 26:
#         break
#     print('new a: {}'.format(a))
#     
# print('Total a: {}'.format(a))

## Пример использоания else в цикле while
# string = input('Enter a string: ')
# char = input('Enter a character: ')
# while string:
#     if string[0] == char:
#         print('yes')
#         break
#     ## Присвоить значение с первого индекса по последний
#     string = string[1:]
# else:
#     print('Nothing')
# 
# greet = 'Hello, world'
# print(len(greet))
# index = -1
# while index < len(greet) - 1:
#     index += 1
#     if greet[index] == ',' or greet[index] == ' ':
#         continue
#     ## функция str.upper() переводит строку в ПРОПИСНЫЕ.
#     print(greet[index].upper(), end=' ')
    
# print()
# print(False == 0) #True
# print(True == 1)  #True
# print(True == -5)   #False
# 
# number = int(input('Enter: '))
# ##number = 1
# number_1, number_2 = number, number
# # 
# while number % 2:
#     print('number: ', number)
#     number //= 2
# else:
#     print('Finish: ', number)
#   
# while not number_1 % 2:
#     print('number_1: ', number_1)
#     number_1 //= 2
# # 
# while number_2:
#     print('number_2: ', number_2)
#     number_2 -= 1

## for элемент последовательности in последовательности:
##     блок инструкций

greet = 'Hello, world' 
for char in greet:
    print(char)
    
for char in greet:
    print(char * 3, end='_')
 

print()    
print(range(10), type(range(10)))
print(range(0, 10, 1)) ## то же самое, что и range(10)
print(5 in range(5))
print(4 in range(5))
# ## range(start, stop, step)
# ## Начало последовательности, конечное значение и шаг
# ## По умолчанию start = 0, step = 1

for item in range(10):
    print(item)
print('-' * 20)
for item in range(4, 10):
    print(item ** .5)
print('-' * 20)   
for item in range(0, 10, 2):
    print('четные: ', item)
print('-' * 20)
for item in range(10, 0, -1):
    print(item)
#     
for i in range(3, len(greet)): ## for i in range(12)
    print('Value of i: ', i)
    if greet[i] == 'w':
        print(f'index of w is {i}')
