a, b, c, d = map(int, input('Введите 4 числа: ').split())
countpl = 0
countmn = 0
if a > 0:
    countpl += 1
elif a < 0 and a != 0 :
    countmn += 1
if b > 0 :
    countpl += 1
elif  b < 0 and b != 0 :
    countmn += 1
if c > 0:
    countpl += 1
elif c < 0 and c != 0 :
    countmn += 1
if d > 0:
    countpl += 1
elif d < 0 and d != 0 :
    countmn += 1
print('число положительных ', countpl)
print('число число отрицательных ', countmn)
