import sys
## Работа с исключениями

# try:
#     ## Блок инструкций
#     print('Before')
#     1 / 0  ## Выполнение try прекращается и начинает работать блок except
#     print('After')
# except:
#     print("You cannot divide by zero!")
# # # 
# print('Done')
# # 
# my_dict = {"a":1, "b":2, "c":3}
# try:
#     value = my_dict["d"]
#     print("You'll never see its message")
# except KeyError:
#     print("That key does not exist!")
# # #     
# # 
# my_list = [1, 2, 3, 4, 5]
# my_dict = {"a":1, "b":2, "c":3}
# try:
#     my_list[6]
#     my_dict[1]
# except (IndexError, KeyError):
#     print('Oops, there is an error')
#     
# 
# my_dict = {"a":1, "b":2, "c":3}
# try:
#     value = my_dict["a"]
#     lst = list(range(4))
#     print(lst[3])
#     a = 1 / 0
# except IndexError:
#     print("This index does not exist!")
# except KeyError:
#     print("This key is not in the dictionary!")
# except:
#     print("Some other error occurred!")
    
# 
my_dict = {"a":1, "b":2, "c":3}
try:
    value = my_dict["p"]
except KeyError:
    print("A KeyError occurred!")
## Блок else отработает только в случае отсутствия исключения
else:
    print("No error occurred!")
#     sys.exit()
## Блок finally отработает в любом случае
finally:
    print("The finally statement всегда отработает!")

## assert проверяет истинность какого-либо выражения
###  код работает дальше
a = 5
b = 7
assert True
# assert a > b, 'Error occured when a > b'  

try:
    assert a > b

except AssertionError:
    print('Условия не выполнилось')
# 
print('All have checked')
# 
try:
    print(1)
    assert 2 + 2 == 4
    print(2)
    assert 1 + 2 == 4
    print(3)  ## это строчка не отработает
except:
    print("assert False.")
finally:
    print("Хорошо")
    
print("Пока")

## Можно создавать свои классы ошибок 
class MyError(Exception):
    print("Ошибка возникла при сравнении моих условий ")

a = 0
b = 7
if a < b:
    ## с помощью raise сами создаем вызов исключения
    raise MyError('a < b error')
if not a:
    raise ZeroDivisionError('Нехорошо вводить нуль при делении')
    






