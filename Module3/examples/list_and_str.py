
a = [1, "2", 3, 4, 5, 6, "hello", 8, 9, 0, '11', True, 5.1]
## Версия 1
for i in a:
    if type(i) == str:
        a.remove(i)
print(a)

## Версия 2
# i = 0
# while i < len(a):
#     if type(a[i]) == str:
#         a.pop(i)
#     i += 1
# print(a)

a.sort()
print(a)