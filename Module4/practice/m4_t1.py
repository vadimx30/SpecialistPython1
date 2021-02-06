#Возвращает периметр и площадь участка.
def piece_of_land(length:float, width:float) -> float:
    perimeter = (length + width)*2
    perimeter = round(perimeter, 2)
    area = length * width
    area = round(area, 2)
    return perimeter, area

#Возвращает итоговую сумму забора.
def fence_price(perimeter:float, cost:float) -> float:
    price = perimeter * cost
    price = round(price, 2)
    return price
    
#Возвращает итоговую сумму земли.
def full_cost(area:float, land_value:float) -> float:
    finalcost = area * land_value
    finalcost = round(finalcost, 2)
    return finalcost
    
