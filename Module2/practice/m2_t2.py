a = int(input('a = '))
b = int(input('b = '))
c = int(input('c = '))
d = int(input('d = '))
e = int(input('e = '))
p = 0 # положительные
n = 0 # отрицательные
if a > 0:
    p += 1
elif a < 0:
    n += 1

if b > 0:
    p += 1
elif b < 0:
    n += 1

if c > 0:
    p += 1
elif c < 0:
    n += 1

if d > 0:
    p += 1
elif d < 0:
    n += 1

if e > 0:
    p += 1
elif e < 0:
    n += 1

print('p = ', p)
print('n = ', n)
