n = int(input('Введите число: '))
if n // 100 == 0:
    a = n // 10
    b = int(n % 10)
    print (a + b)
else:
    a = n // 100
    b = int((n // 10) % 10)
    c = int(n % 10)
    if a > 0 and b > 0 and c > 0:
        print (a * b * c)
    elif a > 0 and b > 0 and c == 0:
        print (a * b)
    elif a > 0 and c > 0 and b == 0:
        print (a * c)
    elif b > 0 and c > 0 and a == 0:
        print (b * c)
    elif a > 0 and b == c == 0:
        print (a)
    elif b > 0 and a == c == 0:
        print (b)
    elif c > 0 and a == b == 0:
        print (c)
