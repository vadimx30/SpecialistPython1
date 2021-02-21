"""
Сформировать данные для отправки заказа из
магазина по накладной и записать в файл:
1) Наименование товара.
2) Количество
3) ФИО покупателя
4) Контактный телефон (10 цифр)
5) Адрес(индекс(ровно 6 цифр), город, улица, дом, квартира)

Эти данные не могут быть пустыми.
Проверить правильность заполнения полей, используя исключения.
"""

import string as st


def item_name() -> str:
    '''Внесение наименования товара в товарную накладную'''
    item_name = input('Наименование товара: ')
    while len(item_name) == 0:
        item_name = input('Наименование товара: ')
    return(f'1) Наименование товара: {item_name}')


def item_count() -> str:
    '''Внесение количества товара в товарную накладную'''
    class NegativeError(Exception):
        pass
    
    try:
        item_count = int(input('Количество товара: '))
        if item_count <= 0:
            raise NegativeError(Exception)
    except ValueError:
        return('!Требуется целое число')
    except NegativeError:
        return('!Требуется положительное число')
    else:
        return(f'2) Количество товара: {item_count} ед.')


def customer_name() -> str:
    '''Внесение ФИО клиента'''
    class DigitsError(Exception):
        pass
    class FIOError(Exception):
        pass
    
    customer_name = input('Фамилия, имя, отчество покупателя: ').split()
    while len(customer_name) == 0:
        customer_name = input('Фамилия, имя, отчество покупателя: ').split()
    try:
        if len(customer_name) != 3:
            raise FIOError(Exception)
        if any(i in st.digits for i in ''.join(customer_name)):
            raise DigitsError(Exception)
    except DigitsError:
        return('!Никаких цифр в ФИО')
    except FIOError:
        return('!Только ФИО через пробел')
    else:
        return(f'3) Фамилия: {customer_name[0]}\n'
               f' Имя: {customer_name[1]}\n'
               f' Отчество: {customer_name[2]}')


def phone_number() -> str:
    '''Внесение телефонного номера клиента в товарную накладную'''
    class NegativeError(Exception):
        pass
    class PhoneCountError(Exception):
        pass    

    try:
        phone_number = int(input('Телефонный номер без пробелов: +7'))
        if phone_number <= 0:
            raise NegativeError(Exception)
        if len(str(phone_number)) != 10:
            raise PhoneCountError(Exception)   
    except ValueError:
        return('!Телефонный номер должен состоять только из цифр')
    except NegativeError:
        return('!Телефонный номер должен состоять только из цифр')
    except PhoneCountError:
        return('!В телефонном номере должно быть 10 цифр')
    else:
        phone_number = str(phone_number)
        return(f'4) Телефонный номер: +7({phone_number[:3]})'
               f'{phone_number[3:6]}-{phone_number[6:8]}'
               f'-{phone_number[8:10]} ')

    
def adress() -> str:
    '''Внесение адреса клиента в товарную накладную'''
    class NegativeError(Exception):
        pass
    class AdressCountError(Exception):
        pass    
    class DigitsError(Exception):
        pass
    
    try:
        adress_ind = int(input('Индекс: '))
        if adress_ind <= 0:
            raise NegativeError(Exception)
        if len(str(adress_ind)) != 6:
            raise AdressCountError(Exception)
        
        city = input('Город: ')
        if any(i in st.digits for i in city):
            raise DigitsError(Exception)        
        
        street = input('Улица: ')
        if any(i in st.digits for i in street):
            raise DigitsError(Exception)
        
        building = int(input('Дом: '))
        if building <= 0:
            raise NegativeError(Exception)
        
        apartment = int(input('Квартира: '))        
        if apartment <= 0:
            raise NegativeError(Exception)

    except ValueError:
        return('!Индекс, номер дома и квартира - должны'
               ' состоять только из цифр')
    except NegativeError:
        return('!Индекс, номер дома и квартира - должны'
               ' состоять только из цифр')
    except AdressCountError:
        return('!В индексе должно быть 6 цифр')
    except DigitsError:
        return('!Никаких цифр в наименовании'
               ' города или улицы')
    else:
        return(f'5) Адрес: {adress_ind}, г.{city}, ул.{street},'
               f' д.{building}, кв.{apartment}')


def main():
    i = 1
    while True:
        with open(('Накладная '+str(i)+'.txt'), 'w') as f:
            print(f'Накладная №{i}')
            f.write(f'Накладная №{i}\n')
            
            f.write(item_name()+'\n')
            
            result = item_count()
            while result[0] == '!':
                print(result)
                result = item_count()
            else:
                f.write(result+'\n')
                      
            result = customer_name()
            while result[0] == '!':
                print(result)
                result = customer_name()
            else:
                f.write(result+'\n')
                    
            result = phone_number()
            while result[0] == '!':
                print(result)
                result = phone_number()
            else:
                f.write(result+'\n')
            
            result = adress()
            while result[0] == '!':
                print(result)
                result = adress()
            else:
                f.write(result)           
        
        i += 1



if __name__ == '__main__':
    main()
