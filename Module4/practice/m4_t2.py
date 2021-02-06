'''
Даны  два  кортежа A и B, каждый  кортеж  состоит  из  N элементов.
Написать функцию для подсчета количества  тех  элементов  кортежа A,  для которых:
1) Ai > Bi
2) Ai = Bi
3) Ai < Bi
'''

def proove(a:tuple,b:tuple):
    d = {'<':0,'=':0,'>':0}
    for i_a in a:
        for i_b in b:
            if i_a > i_b:
                d['>'] +=1
            if i_a < i_b:
                d['<'] +=1
            if i_a == i_b:
                d['='] +=1
    return d


a = tuple(map(int,input('Enter elements of A: ').split()))
b = tuple(map(int,input('Enter elements of B: ').split()))
print(proove(a,b))
