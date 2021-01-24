
# Задача № 1. Получить реверсную запись трехзначного числа
# Пример: 
# вход: 346, выход: 643
# вход: 100, выход: 001# # # id(a) - это адрес переменной a, type(a) - тип переменной
a = 50
b = 7
print('a + b =', a + b)
print('a * b =', a * b)
print('(a ** b) ** 0.5 =', (a ** b) ** 0.5) # Извлечение квадрата
print('Извлечение квадрата с помощью модуля math = %7.3f' % math.sqrt(a))  # the same

# Важный момент
print(a + 1)  # out: 15
print(a)  # out: 10

### Синтаксический сахар
a = a + 1  # a += 1
print('a =', a)
a += 1  # a = a + 1
print('a +=', a)
# Длинная арифметика
a **= 300
print(a)
# 
print(float('inf'))  ## Плюс бесконечность. Самое большое число
print(float('-inf')) ## Минус бесконечность. Самое маленькое число

a = 50
A = 6
 print('a =', a)
 print('A =', A)
# # # id(a) - это адрес переменной a, type(a) - тип переменной
print(id(a), type(a))
print(id(A), type(A))
print(hex(id(a)))
b = 70
B = 6
print(id(b), id(B))
c = 5,1 ### !!! Тип данных не float, а tuple(кортеж))
print(c, type(c))

b = 5.1
print('b =', b)
print('b =', b)
 print(id(b), type(b))
print(10e6)
 c = 'String'
 print('c =', c)
 print(id(c), type(c))
 a = 'Hello'
 print('a = ', a)
 print(id(a), type(a))
 b = 70
 print('b =', b,)
 print(id(b), type(b))
###Пример допустимых переменных и множественного присваивания
int_, float_, str_ = 1, 9.9999, 'python'
 print(int_, float_, str_)
  
data = input() # data - строковая переменная
print(repr(data), type(data))
number = int(data) # number - целочисленная переменная
print('number = ', number, type(number))

## Ввод данных с приглашением и преобразованием к типу int
data_two = int(input('Введите переменную: '))
print(data_two, type(data_two)) 
num_f = float(input()) # num_f - дробная переменная
print('num_f = ', num_f)
#
## 
n = int(input('Введите число: '))
print('n = ', n)

print(number == n) # True или False
print(num_f > n)
print(num_f <= number)
print(number != n)
result = num_f > number
print(result, type(result))

