s = input().split(' ')
x = 0
for i in s:
    if len(i) > x:
        x = len(i)
print(x)
