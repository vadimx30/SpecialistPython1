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

