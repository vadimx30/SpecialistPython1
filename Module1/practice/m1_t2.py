# Задача №2
# Найти каждую цифру трехзначного числа.

number = str(input('Введите трехзначное число: '))
left=int(number[0])
middle=int(number[1])
right =int(number[2])
print ('Первая цифра:',left,
       '\nВторая цифра:',middle,
       '\nТретья цифра:',right)
