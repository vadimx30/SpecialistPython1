"""Module for testing my fuctions"""


def char_counts(string: str) -> dict:
    """Function to count unique characters"""
    string = string.strip()  # удаляет ведущие и конечные пробельные символы
    chars_dict = {}
    for char in string:
        chars_dict.setdefault(char, 0)
        chars_dict[char] += 1
    return chars_dict


def main():
    """Function to use module as script"""
    input_str = input("Enter a string: ")
    print(char_counts(input_str))


def math_func(a: int, b: int) -> int:
    import sys
    if type(a) != int or type(b) != int:
        print('Bad arguments')
        sys.exit(1)
    c = a + b
    d = a * b
    b = a > b
    return c, d, b


def random_args(*args, **kwargs):
    if not args or not kwargs:
        print("There aren't arguments")
    else:
        print(args)
        print(kwargs)


def default_args(number, foundation=2):
    return foundation ** number


def must_one_argument(first, *args):
    print(first)
    print('args:', args)


print(math_func(5, 3))

random_args(5, 'h', name="Student", age=12)


print(default_args(3, 10))  # out -> 10 ** 3 == 1000
print(default_args(3))      # out -> 2 ** 3 == 8
# must_one_argument() ##Выдаст ошибку, обязателен хотя бы один аргумент


# if __name__ == '__main__':
#     main()
