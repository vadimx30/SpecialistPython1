'''
Задача №1 Объемы.
Вход: объемы двух коробок:
a, b, c - длина, ширина и высота первой коробки
k, n, m - длина, ширина и высота первой коробки
толщину коробку не учитывать! 
Коробки можно переворачивать.
Выход: входит ли одна коробка в другую или нет
Ответы: Первая входит во вторую, вторая входит в первую или они не совместимы.
'''

def oslik_ia(abc,kmn):
    if (abc[0] < kmn[0] or abc[0] == kmn[0]) and (abc[1] < kmn[1] or abc[1] == kmn[1]) and (abc[2] < kmn[2] or abc[2] == kmn[2]):
        return True
    else:
        return False
    
def chk_box(abc,kmn):
   aa,bb,cc = abc
   kk,mm,nn = kmn
   if oslik_ia([aa,bb,cc],[kk,mm,nn]) or oslik_ia([aa,cc,bb],[kk,mm,nn]) or oslik_ia([cc,aa,bb],[kk,mm,nn]) or oslik_ia([cc,bb,aa],[kk,mm,nn]): 
       return True
   return False

a,b,c = map(int,input('Enter a,b,c (with space): ').split())
k,m,n = map(int,input('Enter k,m,n (with space): ').split())
if chk_box([a,b,c],[k,m,n]):
    print('Box <abc> put in box <kmn>')
else:
    if chk_box([k,m,n],[a,b,c]):
        print('Box <kmn> put in box <abc>')
    else:
        print('Box <abc> and box <kmn> is not compatible')
