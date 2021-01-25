# Задача №1
# Найти первую и последнюю цифры заданного трехзначного числа.

number = str(input('Введите трехзначное число: '))
left = int(number[0])
right = int(number[2])

print('Первая цифра:', left,
    '\nТретья цифра:', right)


#через math
import math
number = int(input('Введите трехзначное число: '))
left = int(number / 100)
right = int(number % 10)

print('Первая цифра:', left,
    '\nТретья цифра:', right)
