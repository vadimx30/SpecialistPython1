def my_first_func():
    """This is my first function on Python"""
#    import sys
    string = input('Enter the string:')
    symbol = input('Enter the symbol:')
    for char in string:
        if char == symbol:
            print('{}: {}'.format(symbol, string.count(symbol)))
            break
#           sys.exit() # выход из программы
    if not string.count(symbol):
        print('No such a symbol')

## Функция с входными параметрами с хинтингом(подсказка типа)
def my_second_func(string:str, symbol:str) -> int:
    """This is my first function on Python"""
    for char in string:
        if char == symbol:
            return string.count(char)
    return "No found"
 

def main():
    my_first_func()
    a = input("Enter a string: ")
    b = input("Enter a char: ")
    print('Result of second function: ', my_second_func(a, b))


if __name__ == '__main__':
    main()
