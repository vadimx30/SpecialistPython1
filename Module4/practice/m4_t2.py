'''
Даны  два  кортежа A и B, каждый  кортеж  состоит  из  N элементов.
Написать функцию для подсчета количества  тех  элементов  кортежа A,  для которых:
1) Ai > Bi
2) Ai = Bi
3) Ai < Bi
'''
a = (1, 2, 1)
b = (1, 1, 3)
perem_1 = 0
perem_2 = 0
perem_3 = 0

for i in range(len(a)):
    if a[i] > b[i]:
        perem_1 += 1
    elif a[i] == b[i]:
        perem_2 += 1
    elif a[i] < b[i]:
        perem_3 += 1
    
print(perem_1, perem_2, perem_3)
