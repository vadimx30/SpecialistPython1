a = int(input('Введите трехзначное число: '))
b = (a//100)
c = (a - a//10*10)
d = (a - b*100 - c)//10
print(b)
print(d)
print(c)
