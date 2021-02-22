"""
Написать функцию для сложения двух аргументов, в которую нужно
добавить обработку исключений для случаев сложения str с int, float и bool
"""
def div(a,b):
    try:
        return  a+b
    except Exception as ext:
        return(ext)
        
print(div(1,'d'))
