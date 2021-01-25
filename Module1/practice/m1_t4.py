# Задача №4
"""
Вход:
    расстояние(50 - 10000 км),
    расход в литрах (5-25 литров) на 100 км и
    стоимость бензина(константа) = 48 руб

Выход: стоимость поездки в рублях
"""
import math
distance = int(input('Введите расстояние (50 - 10000 км): '))
fuel_consumption100 = int(input('Введите расход топлива (5 - 25 литров/100км): '))
fuel_consumption1 = float(fuel_consumption100/100)
fuel_price = int(48)
trip_cost = float(round((distance * fuel_consumption1 * fuel_price), 2))
print('Стоимость поездки составляет ', trip_cost, 'рублей')
