def test_gen():
    x = 2
    y = 3
    print('Первый yield')
    print(locals())  # Словарь всех переменных функции
    yield x, y

    x *= 2
    print('Второй yield')
    print(locals())
    yield x, y

    x *= 2
    print('Последний yield')
    print(locals())
    yield x, y


# ## Вызов генератора
iter = test_gen()
print(iter)

# ## Вызов первого yield
next(iter)

# ## Вызов второго yield
next(iter)

# ## Вызов последнего yield
next(iter)
next(iter, 0)
