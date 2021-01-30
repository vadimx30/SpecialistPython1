
a = n // 1000
b = int((round(n)/100) % 10)
c = int((n // 10) % 10)
d = int(n % 10) 

if a == d:
    if b == c:
        print ( n,'- палиндром')
    else:
        print ( n,'- не палиндром')
else:
    print ( n,'- не палиндром')
