import sys

def my_funcs():
    n = input("Введите трехзначное число: ")
    res=''
    for i in n:
        res = i + res
        
    print (f"Реверсная 'запись' числа {n} равна {res}")
    print(locals())
    print('id(res)', id(res))
    # the same
    # print(f'Result: {n[2]}{n[1]}{n[0]}')


def my_funcs_2():
    n = input("Введите трехзначное число: ")
    res=''
    for i in n:
        res = i + res
        
    return res
    
    
def input_func(n: str) -> str:
    """ Reverse a number """
    res=''
    for i in n:
        res = i + res
        
    return res


def input_func_2(n='123') -> int:
    """ Reverse a number """
    res=''
    for i in n:
        res = i + res
        
    return res

def func():
    string = 'astuhasth'
    for char in string:
        if char == 't':
            print('Finish')
            return None
        else:
            print(char)
            
            
my_funcs()
res = my_funcs_2()
print('id(res) ', id(res))
print(res)
func()
print(input_func(res))
print(input_func_2('567'))
