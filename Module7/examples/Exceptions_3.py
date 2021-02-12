import sys

# def read_and_divide(filename):
#   print("before " + filename)
#   with open(filename, 'r') as fh:
#       number = int(fh.readline())
#       print('number: ', number)
#       print(100 / number)
#   print("after " + filename)
#   print()
# 
# files = sys.argv[1:]
# 
# for filename in files:
#     try:
#         read_and_divide(filename)
#     except Exception as err:
#         print(" There was a problem in " + filename)
#         print(" Text: {}".format(err))
#         print(" Name: {}".format(type(err).__name__))
# 
# ## IOError - отработка при доступе к несуществующему файлу
# for filename in files:
#     try:
#         read_and_divide(filename)
#     except (ZeroDivisionError, IOError):
#         print("We have a problem with file {}".format(filename))

#### Блок finally отработает в любом случае!
# def div(a, b):
#     try:
#         print("try")
#         c = a / b
#     except Exception:
#         print("exception")
#         sys.exit(1)
#         return 1
#     finally:
#         print("finally")
# 
# div(2, 1)
# print('-' * 20)
# div(2, 0)


