# Задача №1
# Найти первую и последнюю цифры заданного трехзначного числа.

number = int(input('Введите трехзначное число: '))
string=str(number)
left=int(string[0])
right =int(string[2])
print ('Первая цифра:',left,'\nТретья цифра:',right)
