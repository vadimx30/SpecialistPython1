# Задача №3
# Найти каждую цифру четырехзначного числа.
import math
number = int(input('Введите четырехзначное число: '))
left1 = int(number / 1000)
left2 = int((number - left1 * 1000) // 100)
right1 = int(number % 100 // 10)
right2 = int(number % 10)

print('Первая цифра:', left1, 
    '\nВторая цифра:', left2, 
    '\nТретья цифра:', right1, 
    '\nЧетвертая цифра:', right2)
