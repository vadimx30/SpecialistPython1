'''
Даны  два  кортежа A и B, каждый  кортеж  состоит  из  N элементов.
Написать функцию для подсчета количества  тех  элементов  кортежа A,  для которых:
1) Ai > Bi
2) Ai = Bi
3) Ai < Bi
'''
a = input('enter:').split()
b = input('enter:').split()
c = 0
d = 0
e = 0
for i in range(len(a)):
    if a[i] > b[i]:
        c +=1
    if a[i] == b[i]:
        d +=1
    if a[i] < b[i]:
        e +=1
print(c)
print(d)
print(e)
